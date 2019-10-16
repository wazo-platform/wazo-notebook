# Zuul procedures

## How to add a new github repository under Zuul monitoring

- make a PR to modify wazo-platform/sf-config to change the file
  [resources/resources.yaml](https://github.com/wazo-platform/sf-config/blob/master/resources/resources.yaml) to add the targeted repository in the
  source-repositories section.
- enable [branch protection](https://zuul.wazo.community/docs/user/zuul_user.html#zuul-github-branch-protection) on your repo
- create the `mergeit` label for the repository.
- create a PR to add a `zuul.conf` file like in [wazo-platform/wazo-webhookd](https://github.com/wazo-platform/wazo-webhookd/blob/master/zuul.yaml)

## How to merge a PR using Zuul

- add the `mergeit` label for the PR.
- review the change.
- Zuul will merge the PR automatically.

## How to write a new job in Zuul

- if the job is specific to this repo, add it directly in the repo
  - create `pre.yaml` and `run.yaml`
  - see [wazo-ansible](https://github.com/wazo-platform/wazo-ansible) as an example
- if the job is reusable elsewhere, add the job definition in [sf-jobs/zuul.d/wazo.yaml](https://github.com/wazo-platform/sf-jobs/blob/master/zuul.d/wazo.yaml)
  - Job parents available in Software Factory: [openstack-infra/zuul-jobs](https://github.com/openstack-infra/zuul-jobs/tree/master/roles)

Notes:

- the `pre-run` stage is aimed at configuring the environment for running a test. On failure, retry at most 3 times.
- the `run` stage is aimed at running the test. On failure, stop everything and report.
- the `post-run` stage is aimed at collecting logs and artifacts.

## Details

- See the [definition of the Zuul pipeline](https://github.com/wazo-platform/sf-config/blob/master/zuul.d/_pipelines.yaml#L46-L56) for the exact requirements for Zuul to merge a PR.

## Images

- VM images are defined in [wazo-platform/sf-config/nodepool/elements/virt-customize](https://github.com/wazo-platform/sf-config/tree/master/nodepool/elements/virt-customize).
- runc container images are defined in [wazo-platform/sf-config/nodepool/runC](https://github.com/wazo-platform/sf-config/tree/master/nodepool/runC).

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

### SSH node
* Check the node IP at the beginning of job output
* From `root@zuul.wazo.community`
    * `ssh zuul-worker@<zuul_node_ip> -i /var/lib/software-factory/bootstrap-data/ssh_keys/zuul_rsa`

### Keep node running after job end
* Check the `job_id` from the URL of the job ouput.
    ex: `https://zuul.wazo.community/zuul/t/local/stream/9eecc3177cbb45d39d9aeb5430146a34?logfile=console.log`
        The `job_id` is `9eecc3177cbb45d39d9aeb5430146a34`
* From `root@zuul.wazo.community`
    * `zuul autohold --tenant local --project wazo-platform/<repository> --job <job_id> --reason debug`
    * Do what you want to do and delete node after
    * `nodepool list | grep <zuul_node_ip>`
    * `nodepool delete <node_id>`

### Removing a dandling job

* From `root@zuul.wazo.community`
    * `zuul dequeue --tenant local --pipeline <pipeline> --project <project> --change <pr number>,<sha1>`
    * For example: `zuul dequeue --tenant local --pipeline check --project wazo-platform/wazo-websocketd --change 8,e2680cb6eac37de5b63710c3427261ffd38e18a9`
