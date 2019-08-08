# Renaming a git repository

## All repositories

* Files
  * all files/import in the package
* Debian package name
  * `debian/control`
    * add Provides, Conflicts and Replaces for the former name
  * `debian/changelog`
    * clean version numbers: "8:18.05..." -> "18.05..."
    * add a changelog entry stating the rename
  * `debian/<package-name>.*`
* xivo-build-tools
  * `etc/xivo-build-tools/packages`
* xivo-upgrade:
  * purge old package
* xivo-tools:
  * `dev-tools/repos/python-tag`
  * `dev-tools/repos/all`
  * `dev-tools/repos/shortlog`
* wazo-doc
* wazo-ansible
* Github repository
* Jenkins job
   * `<package-name>`
   * `daily-integration-tests`
* sf-config
  * `resources/resources.yaml`
* wazo-acceptance
* wazo-sdk
  * `project.yml`
* Debian dependencies for other packages
* requirements.txt for other packages
* Remove old package from wazo-dev-stretch distribution
* announce to other devs so that they can update their local repo
  * `git remote set-url origin git@github.com:wazo-pbx/<new-name>`

Note: the following items are linked and must be renamed at the same time (or the build will fail):
* Debian package name
* xivo-build-tools
* Github repo name
* Jenkins job name

## Service repository

* Files
  * `/etc/<service-name>`
  * `/var/run/<service-name>/<service-name>.pid`
  * `/var/log/<service-name>.log`
  * root package in the source code `<service_name>`
  * Source directory in Dockerfile `/usr/src/<service-name>`
* Debian package name
  * `debian/<package-name>.postinst`:
    * rename log files, including rotated log files
  * system user
* Docker image names `wazopbx/<service-name>`
  * remove old image from docker hub
* wazo-platform
  * `debian/control`: Depends
* xivo-backup
* wazo-service
* xivo-utils:
  * `sbin/wazo-reset`
* xivo-swagger-doc
* xivo-monitoring
* wazo-auth-keys
* Translations
