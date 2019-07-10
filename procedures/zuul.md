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

## Details

- See the [definition of the Zuul pipeline](https://github.com/wazo-pbx/sf-config/blob/master/zuul.d/_pipelines.yaml#L46-L56) for the exact requirements for Zuul to merge a PR.