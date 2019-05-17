# Renaming a service

* `<service-name-repository>`
  * `/etc/<service-name>`
  * `/var/run/<service-name>/<service-name>.pid`
  * `/var/log/<service-name>.log`
  * root package in the source code `<service_name>` 
  * Source directory in Dockerfile `/usr/src/<service-name>`
  * Debian package name
    * debian/control
    * debian/changelog
      * remove "clean" version numbers "8:18.05..." -> "18.05..."
    * debian/<service-name>.*
    * system user
* Docker image names `wazopbx/<service-name>`
  * remove old image from docker hub
* xivo-backup
* xivo-service
* xivo-build-tools
* xivo-tools: repo list
* xivo-utils : wazo-reset
* xivo-upgrade: purge old package
* wazo-doc
* swagger-doc
* monitoring
* ansible
* wazo-acceptance
* jenkins job
   * `<service-name>`
   * `daily-integration-tests`
* translations
