# Zuul procedures

## How to add a new github repository under Zuul monitoring

- make a PR to modify wazo-pbx/sf-config to change the file
  [resources/resources.yaml](https://github.com/wazo-pbx/sf-config/blob/master/resources/resources.yaml) to add the targeted repository in the
  source-repositories section.
- enable [branch protection](https://zuul.wazo.community/docs/user/zuul_user.html#zuul-github-branch-protection) on your repo
- create the `mergeit` label for the repository.
- create a PR to add a `zuul.conf` file like in [wazo-pbx/wazo-webhookd](https://github.com/wazo-pbx/wazo-webhookd/blob/master/zuul.yaml)

## How to merge a PR using Zuul

- add the `mergeit` label for the PR.
- review the change.
- Zuul will merge the PR automatically.

## How to write a new job in Zuul

- if the job is specific to this repo, add it directly in the repo
  - create `pre.yaml` and `run.yaml`
  - see [wazo-ansible](https://github.com/wazo-pbx/wazo-ansible) as an example
- if the job is reusable elsewhere, add the job definition in [sf-jobs/zuul.d/wazo.yaml](https://github.com/wazo-pbx/sf-jobs/blob/master/zuul.d/wazo.yaml)
  - Job parents available in Software Factory: [openstack-infra/zuul-jobs](https://github.com/openstack-infra/zuul-jobs/tree/master/roles)

Notes:

- the `pre` stage is aimed at configuring the environment for running a test. On failure, retry at most 3 times.
- the `run` stage is aimed at running the test. On failure, stop everything and report.


## Details

- See the [definition of the Zuul pipeline](https://github.com/wazo-pbx/sf-config/blob/master/zuul.d/_pipelines.yaml#L46-L56) for the exact requirements for Zuul to merge a PR.

## Debugging

### Zuul fails to start

* Check `/var/log/zuul/scheduler.log`
* Ensure you don't have the same job name twice in master across repos: when Zuul starts, it checks all repos, reading the `zuul.yaml` in branch master. If two jobs have the same name, Zuul will not start.

### Problem building an image

* Check `/var/log/nodepool`
* Check `/var/www/nodepool-log`

### My dependency in `bindep.txt` is not installed

`bindep.txt` files are only applicable to virtual machine images, not runc containers

### More commands

* `zuul show`
* `nodepool list`
