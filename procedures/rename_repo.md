# Renaming a git repository

* `<service-name-repository>`
  * `/etc/<service-name>`
  * `/var/run/<service-name>/<service-name>.pid`
  * `/var/log/<service-name>.log`
  * root package in the source code `<service_name>`
  * Source directory in Dockerfile `/usr/src/<service-name>`
* Debian package name
  * `debian/control`
    * add Provides, Conflicts and Replaces for the former name
  * `debian/changelog`
    * remove "clean" version numbers "8:18.05..." -> "18.05..."
    * add a changelog entry stating the rename
  * `debian/<package-name>.postinst`:
    * rename log files
  * `debian/<package-name>.*`
  * system user
* Docker image names `wazopbx/<service-name>`
  * remove old image from docker hub
* wazo-platform
  * `debian/control`: Depends
* xivo-backup
* xivo-service
* xivo-build-tools
  * `etc/xivo-build-tools/packages`
* xivo-tools:
  * `dev-tools/repos/python-tag`
  * `dev-tools/repos/all`
  * `dev-tools/repos/shortlog`
* xivo-utils: wazo-reset
* xivo-upgrade: purge old package
* wazo-doc
* xivo-swagger-doc
  * `debian/control`: Depends
* monitoring
* wazo-ansible
* wazo-auth-keys
* wazo-acceptance
* sf-config
  * `resources/resources.yaml`
* jenkins job
   * `<package-name>`
   * `daily-integration-tests`
* translations
* wazo-sdk
  * `project.yml`
