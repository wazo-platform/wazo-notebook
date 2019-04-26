Note: If you update this document, please also update checklist-remove-repo.md, if applicable

- Create repo on Github
- In Github repo settings, add a webhook with URL https://jenkins.wazo.community/github-webhook/

OR

- Run script xivo-tools/dev-tools/new-repo

THEN

- Add repo in xivo-build-tools/etc/packages
- Add repo in xivo-tools/dev-tools/repos si ce n'est pas un repo \*-packaging
- Add job on Jenkins
- Add job for integration tests in daily-integration-tests on Jenkins
