# Wazo Git workflow

* [Trunk-based development](https://trunkbaseddevelopment.com/): branch `master`
* Feature branches: small, short-lived branches are merged into master. 
* Branch naming: Example: `w493-dhcp-config`. Convention: `w493` = Jira ticket ID, `dhcp-config` = arbitrary description of the branch.
* Peer-review: a developer should not merge her/his own branches into master. Another developer should review a branch before merging.
* Rebase: Branches should be rebased before merging.
* Merge: Branches across multiple repositories should be merged using a merge commit (not fast-forward). Benefits:
  * finding more easily which commits belonged to which feature-branch.
  * knowing who reviewed and merged the feature-branch
* Tags: Each release of Wazo must be tagged in applicable repositories. Tags must be PGP-signed.

## Exceptions

wazo-doc: long-lived branch "production" is considered the stable branch, while master is considered the development branch, in order for Readthedocs to have two rolling versions.
