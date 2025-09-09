#!/usr/bin/env python3
from __future__ import annotations

import re
from collections.abc import Generator
from typing import Any

import os
import sys
import yaml
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from functools import cached_property

import requests


ZUUL_APP_ID = 105_849
WAZO_PLATFORM = 'wazo-platform'
RELEASES = ('bookworm', 'trixie', 'forky')


@dataclass
class Branch:
    name: str
    protected: bool
    latest_commit_sha: str

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> Branch:
        return cls(data['name'], data['protected'], data['commit']['sha'])

    def __str__(self) -> str:
        negation = '' if self.protected else 'not '
        return f'Branch "{self.name}" is {negation}protected. Latest commit: {self.latest_commit_sha}'


class Session:
    def __init__(self, args: Namespace) -> None:
        self._args = args
        self.organization = args.organization

    @cached_property
    def token(self) -> str:
        config = load_config()
        if not (token := config.get('github_token')):
            raise RuntimeError('Unable to read github_token from WDK config file')
        return token

    @cached_property
    def default_headers(self) -> dict[str, str]:
        return {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def request(self, path: str = '', method: str = 'get', **kwargs) -> dict[str, Any] | None:
        url = f'https://api.github.com/{path}'
        kwargs['headers'] = self.default_headers
        r = getattr(requests, method)(url, **kwargs)
        if r.status_code in (404, 204):
            return None
        return r.json()

    def paginated_request(self, path: str, **kwargs: Any) -> list[dict[str, Any]]:
        next_url = f'https://api.github.com/{path}'
        results = []
        while next_url is not None:
            r = requests.get(next_url, headers=self.default_headers, **kwargs)
            r.raise_for_status()
            results.extend(r.json())
            try:
                next_url = re.search(r'(?<=<)(\S*)(?=>; rel="next")', r.headers.get('link', ''), re.IGNORECASE)[0]
            except TypeError:
                next_url = None
        return results

    def iter_organization_repos(self, include_archived: bool = False) -> Generator[ProjectRepository, None, None]:
        for repo in self.paginated_request(f'orgs/{self.organization}/repos', params={'per_page': 100}):
            if repo["archived"] and not include_archived:
                continue
            yield ProjectRepository(
                repo['name'],
                self.organization,
                self._args.debian_release,
                self
            )

    def iter_repos(self) -> Generator[ProjectRepository, None, None]:
        if self._args.repo:
            yield ProjectRepository.from_args(self._args, self)
        else:
            yield from self.iter_organization_repos(include_archived=False)


@dataclass
class ProjectRepository:
    name: str
    organization: str
    debian_release: str
    session: Session

    @classmethod
    def from_args(cls, args: Namespace, session: Session) -> ProjectRepository:
        return cls(
            name=args.repo,
            organization=args.organization,
            debian_release=args.debian_release,
            session=session,
        )

    def repo_request(
        self,
        path: str | None = None,
        method: str = 'get',
        **kwargs: Any
    ) -> dict[str, Any] | list[dict[str, Any]] | None:
        suffix = f'/{path.lstrip("/")}' if path else ''
        return self.session.request(
            f'repos/{self.organization}/{self.name}{suffix}',
            method=method,
            **kwargs,
        )

    @cached_property
    def branches(self) -> dict[str, Branch]:
        return {
            branch['name']: Branch.from_data(branch)
            for branch in self.session.paginated_request(
                f'repos/{self.organization}/{self.name}/branches'
            )
        }

    @cached_property
    def default_branch_name(self) -> str:
        return 'main' if 'main' in self.branches else 'master'

    @property
    def has_zuul(self) -> bool:
        return self.organization == WAZO_PLATFORM

    @cached_property
    def default_branch(self) -> Branch:
        return self.branches[self.default_branch_name]

    @cached_property
    def release_branch(self) -> Branch | None:
        return self.branches.get(self.debian_release, None)

    def get_release_diff(self) -> dict[str, Any] | None:
        return self.repo_request(f'compare/{self.default_branch_name}...{self.debian_release}')

    def unprotect_release_branch(self) -> None:
        self.repo_request(f'branches/{self.debian_release}/protection', method='delete')


def create(args: Namespace, session: Session) -> None:
    """Create release branch with protections."""
    repo = ProjectRepository.from_args(args, session)
    if repo.release_branch is not None:
        print(f'Debian {repo.debian_release} branch already exists.')
        sys.exit(1)
    repo.repo_request('git/refs', method='post', json={
        "ref": f'refs/heads/{repo.debian_release}',
        "sha": repo.default_branch.latest_commit_sha,
    })
    protect(args, session)
    print(f'New protected branch "{repo.debian_release}" created')


def protect(args: Namespace, session: Session) -> None:
    """Add branch protections to release branch."""
    repo = ProjectRepository.from_args(args, session)
    if repo.release_branch is None:
        print(f'No debian {repo.debian_release} branch exists. Please create.')
        sys.exit(1)
    if repo.release_branch.protected is True:
        print(f'Debian {repo.debian_release} branch is already protected')
        sys.exit(0)

    repo.repo_request(
        f'branches/{repo.debian_release}/protection',
        method='put',
        json={
            'enabled': True,
            'enforce_admins': None,
            'required_status_checks': {
                'strict': True,
                'checks': [{'context': 'local/check', 'app_id': ZUUL_APP_ID}]
            } if repo.has_zuul else None,
            'required_pull_request_reviews': {
                'dismiss_stale_reviews': True,
                'require_last_push_approval': False,
                'required_approving_review_count': 1
            },
            'restrictions': None,
        }
    )
    print(f'Debian {repo.debian_release} branch is now protected')


def unprotect(args: Namespace, session: Session) -> None:
    """Remove branch protections from release branch."""
    repo = ProjectRepository.from_args(args, session)
    if repo.release_branch is None:
        print(f'No debian release branch exists. Please create.')
        sys.exit(1)
    if repo.release_branch.protected is False:
        print(f'Debian {repo.debian_release} branch is already unprotected')
        sys.exit(0)
    repo.unprotect_release_branch()
    print(f'Debian {repo.debian_release} branch is now unprotected')


def delete(args: Namespace, session: Session) -> None:
    repo = ProjectRepository.from_args(args, session)
    if repo.release_branch is None:
        print(f'No debian release branch exists. Nothing to do.')
        sys.exit(0)

    if repo.release_branch.protected is True:
        print(f'Debian {repo.debian_release} branch is protected. Unprotect first.')
        sys.exit(0)

    response = input(f"Are you sure you want to delete the branch '{repo.debian_release}'? [y/N] ")
    if response.lower() != 'y':
        print('Ok, not deleting.')
        sys.exit(0)

    repo.repo_request(f'git/refs/heads/{repo.debian_release}', method='delete')
    print(f'Debian {repo.debian_release} branch was deleted')


def info(args: Namespace, session: Session) -> None:
    repo = ProjectRepository.from_args(args, session)
    for branch in repo.branches.values():
        print(branch)


def list_branches(args: Namespace, session: Session) -> None:
    for repo in session.iter_organization_repos(args.include_archived):
        if args.outdated is False:
            if not repo.release_branch:
                continue
            print(repo.name)
            continue
        try:
            diff = repo.get_release_diff()
        except requests.HTTPError as e:
            continue
        if diff and diff['status'] == "behind":
            print(f'{repo.name} is behind by {diff["behind_by"]} commit(s)')
        else:
            print(f'{repo.name} is up to date')


COMMANDS = {
    'create': create,
    'protect': protect,
    'unprotect': unprotect,
    'delete': delete,
    'info': info,
    'list': list_branches,
}


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    common = ArgumentParser(add_help=False)
    common.add_argument(
        '-o',
        '--organization',
        default=WAZO_PLATFORM,
        choices=[WAZO_PLATFORM, 'wazo-communication', 'TinxHQ'],
        help='GitHub organization',
    )
    common.add_argument('-r', '--debian-release', default='bookworm', choices=RELEASES, help='Debian release name')
    subparsers = parser.add_subparsers(dest='command', help='Action to perform')
    repo_required = ArgumentParser(add_help=False)
    repo_required.add_argument('repo', metavar='REPOSITORY', help='Repository name')
    for option in ('create', 'protect', 'unprotect', 'delete', 'info'):
        subparsers.add_parser(option, parents=[common, repo_required])
    list_parser = subparsers.add_parser('list', parents=[common], help='List repos with release branches')
    list_parser.add_argument('-a', '--include-archived', action='store_true', help='Include archived repos')
    list_parser.add_argument('--outdated', action='store_true', help='List outdated only')
    return parser


def load_config() -> dict[str, Any]:
    config_path = os.getenv('WDK_CONFIG_FILE', os.path.expanduser('~/.config/wdk/config.yml'))
    try:
        with open(config_path) as f:
            return yaml.safe_load(f)
    except IOError:
        raise RuntimeError('Unable to read WDK config file.')


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    handle_command = COMMANDS[args.command]
    handle_command(args, Session(args))


if __name__ == '__main__':
    main()
