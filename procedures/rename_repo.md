# Renaming a git repository

## Common

* `<repository-name>`
  * all files/import in the package
* Debian package name
  * `debian/control`
    * add Provides, Conflicts and Replaces for the former name
  * `debian/changelog`
    * remove "clean" version numbers "8:18.05..." -> "18.05..."
    * add a changelog entry stating the rename
  * `debian/<package-name>.*`
* xivo-build-tools
  * `etc/xivo-build-tools/packages`
* xivo-upgrade: purge old package
* xivo-tools:
  * `dev-tools/repos/python-tag`
  * `dev-tools/repos/all`
  * `dev-tools/repos/shortlog`
* wazo-doc
* wazo-ansible
* jenkins job
   * `<package-name>`
   * `daily-integration-tests`
* sf-config
  * `resources/resources.yaml`
* wazo-acceptance
* wazo-sdk
  * `project.yml`

## Service

* `<service-name-repository>`
  * `/etc/<service-name>`
  * `/var/run/<service-name>/<service-name>.pid`
  * `/var/log/<service-name>.log`
  * root package in the source code `<service_name>`
  * Source directory in Dockerfile `/usr/src/<service-name>`
* Debian package name
  * `debian/<package-name>.postinst`:
    * rename log files
  * system user
* Docker image names `wazopbx/<service-name>`
  * remove old image from docker hub
* wazo-platform
  * `debian/control`: Depends
* xivo-backup
* xivo-service
* xivo-utils: wazo-reset
* xivo-swagger-doc
  * `debian/control`: Depends
* monitoring
* wazo-auth-keys
* translations
