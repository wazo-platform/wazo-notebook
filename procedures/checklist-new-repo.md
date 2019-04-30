Note: If you update this document, please also update checklist-remove-repo.md, if applicable

- Create repo on Github
- In the repo's settings, add a webhook
  - Payload URL: 
    - open source code: `https://jenkins.wazo.community/github-webhook/`
    - private code: `https://jenkins.wazo.io/github-webhook/`
  - Content Type: `x-www-form-urlencoded`
  - Secret: none
  - Select trigger events: 
    - `Pushes`, 
    - `Pull requests`

OR

- Run script xivo-tools/dev-tools/new-repo

THEN

- Add repo in xivo-build-tools/etc/packages
- Add repo in xivo-tools/dev-tools/repos si ce n'est pas un repo \*-packaging
- Add job on Jenkins
- Add job for integration tests in daily-integration-tests on Jenkins
