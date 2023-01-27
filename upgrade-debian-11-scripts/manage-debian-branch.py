#!/usr/bin/env python3
from __future__ import annotations

from typing import Any

import json
import os
import sys
import yaml
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from functools import cached_property

import requests


ZUUL_APP_ID = 105_849
WAZO_PLATFORM = 'wazo-platform'


@dataclass
class ProjectRepository:
    repo: str
    organization: str
    debian_release: str

    @cached_property
    def token(self) -> str:
        config = load_config()
        if not (token := config.get('github_token')):
            raise RuntimeError('Unable to read github_token from WDK config file')
        return token

    @classmethod
    def from_args(cls, args: Namespace) -> ProjectRepository:
        return cls(repo=args.repo, organization=args.organization, debian_release=args.debian_release)

    def request(self, path: str = '', method: str = 'get', **kwargs) -> dict[str, Any] | None:
        suffix = f'/{path.lstrip("/")}' if path else ''
        url = f'https://api.github.com/repos/{self.organization}/{self.repo}{suffix}'
        kwargs['headers'] = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        r = getattr(requests, method)(url, **kwargs)
        if r.status_code in (404, 204):
            return None
        return r.json()

    @cached_property
    def default_branch_name(self) -> str:
        return self.request()['default_branch']

    @property
    def has_zuul(self) -> bool:
        return self.organization == WAZO_PLATFORM

    def get_default_branch(self) -> dict[str, Any] | None:
        return self.request(f'branches/{self.default_branch_name}')

    def get_release_branch(self) -> dict[str, Any] | None:
        return self.request(f'branches/{self.debian_release}')

    def get_branch_protection(self, branch: str) -> dict[str, Any]:
        return self.request(f'branches/{branch}/protection')

    def unprotect_release_branch(self) -> None:
        self.request(f'branches/{self.debian_release}/protection', method='delete')


def create(repo: ProjectRepository) -> None:
    """Create release branch with protections."""
    release_branch = repo.get_release_branch()
    if release_branch is not None:
        print(f'Debian {repo.debian_release} branch already exists.')
        sys.exit(1)
    default_branch = repo.get_default_branch()
    repo.request('git/refs', method='post', json={
        "ref": f'refs/heads/{repo.debian_release}',
        "sha": default_branch['commit']['sha'],
    })
    protect(repo)
    print(f'New protected branch "{repo.debian_release}" created')


def protect(repo: ProjectRepository) -> None:
    """Add branch protections to release branch."""
    release_branch = repo.get_release_branch()
    if release_branch is None:
        print(f'No debian {repo.debian_release} branch exists. Please create.')
        sys.exit(1)
    if release_branch['protected'] is True:
        print(f'Debian {repo.debian_release} branch is already protected')
        sys.exit(0)

    repo.request(
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


def unprotect(repo: ProjectRepository) -> None:
    """Remove branch protections from release branch."""
    release_branch = repo.get_release_branch()
    if release_branch is None:
        print(f'No debian release branch exists. Please create.')
        sys.exit(1)
    if release_branch['protected'] is False:
        print(f'Debian {repo.debian_release} branch is already unprotected')
        sys.exit(0)
    repo.unprotect_release_branch()


def delete(repo: ProjectRepository) -> None:
    release_branch = repo.get_release_branch()
    if release_branch is None:
        print(f'No debian release branch exists. Nothing to do.')
        sys.exit(0)

    if release_branch['protected'] is True:
        print(f'Debian {repo.debian_release} branch is protected. Unprotect first.')
        sys.exit(0)

    response = input(f"Are you sure you want to delete the branch '{repo.debian_release}'? [y/N] ")
    if response.lower() != 'y':
        print('Ok, not deleting.')
        sys.exit(0)

    repo.request(f'git/refs/heads/{repo.debian_release}', method='delete')
    print(f'Debian {repo.debian_release} branch was deleted')


def info(repo: ProjectRepository) -> None:
    print(json.dumps(repo.get_release_branch(), indent=4))


COMMANDS = {
    'create': create,
    'protect': protect,
    'unprotect': unprotect,
    'delete': delete,
    'info': info,
}


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('repo', metavar='REPOSITORY', help='Repository name')
    parser.add_argument('command', choices=list(COMMANDS), help='Action to perform')
    parser.add_argument(
        '-o',
        '--organization',
        default=WAZO_PLATFORM,
        choices=[WAZO_PLATFORM, 'wazo-communication', 'TinxHQ'],
        help='GitHub organization',
    )
    parser.add_argument('-r', '--debian-release', default='bullseye', help='Debian release name')
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
    project = ProjectRepository.from_args(args)
    handle_command(project)


if __name__ == '__main__':
    main()
