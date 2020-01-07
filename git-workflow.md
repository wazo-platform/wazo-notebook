# Wazo Git workflow

* [Trunk-based development](https://trunkbaseddevelopment.com/): branch `master` ;
* Feature branches: small, short-lived branches are merged into master ;
* Branch naming: Example: `w493-dhcp-config`. Convention: `w493` = Jira ticket ID, `dhcp-config` = arbitrary description of the branch ;
* Peer-review: a developer should not merge her/his own branches into master. Another developer should review a branch before merging ;
* Choose a merging strategy (cf. below) based on your context ;
* Tags: Each release of Wazo must be tagged in applicable repositories. Tags must be PGP-signed.

## Reviewing and validating pull request

* PR owner: set JIRA ticket to `in review`
* PR owner: add the `mergeit` label to mark the PR as ready to review
* PR owner: assign to someone, if no JIRA ticket exists
* Reviewer: review the PR on Github
  * There must be at least one reviewer. Reviewers may request other reviewers.
  * Reviewers should not have written code in the PR
  * Fetch PR locally:

		git pull-request --download <PR-number>

* Reviewer: mark all conversations as `resolved` with the decision inside the conversation
* Reviewer: once the PR is reviewed and approved, "Approve" it on Github (in Review tab)
* Zuul: run tests and merge (if tests pass).
* [while !Zuul] Reviewer: merge the PR manually


## Merging Strategies

read: [Git Merge vs. Rebase: What’s the Diff?](https://hackernoon.com/git-merge-vs-rebase-whats-the-diff-76413c117333), [Github: About pull request merges](https://help.github.com/en/articles/about-pull-request-merges#rebase-and-merge-your-pull-request-commits).

### Rebase

Branches should be [rebased before merging](https://help.github.com/en/articles/about-pull-request-merges#rebase-and-merge-your-pull-request-commits) ;
* Benefits: clean linear commit history
* Pull request's branch should be deleted as it history appear on base branch and in order to keep a clean tree.

### Merge

Branches across multiple repositories should be merged using a merge commit (not fast-forward).

* Benefits:
  * finding more easily which commits belonged to which feature-branch.
  * knowing who reviewed and merged the feature-branch

## Exceptions

`wazo-doc`: long-lived branch `production` is considered the stable branch, while `master` is considered the development branch, in order for Readthedocs to have two rolling versions.
