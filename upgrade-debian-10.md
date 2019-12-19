# Upgrade from Debian 9 (Stretch) to Debian 10 (Buster)

This document is a dump of the Etherpad we used during Stretch to Buster upgrade.

## Dump

* restore apt-mark for packages upgraded with apt install in wazo-upgrade and wazo-dist-upgrade
* make tox run on py37
  * add ppa py37 on jenkins.wazo.community (https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)

* systemd units: replace /var/run with /run
* debian packaging: remove dh-systemd and use debhelper >= 9.20160709 in the control

* move in readme: https://zuul.wazo.community/etherpad/p/engine-upgrade

* find why dahdi-linux-modules is not reproducible in buster
* remove old dahdi-linux-modules in buster distro
* build dahdi-linux-modules-686-pae in buster

* copy this pad to notebook/buster

* Remove scripts from wazo-upgrade https://github.com/wazo-platform/wazo-upgrade/pull/9
* StyleGuide upgrade scripts
  * prefix scripts with two digits
  * use only "-" in the scripts name
  * always keep file extensions

* upgrade docker-compose.yml commented path to use python3 instead of python3.5

* remove backports and packages now packaged by Debian
  * https://github.com/wazo-platform/xivo-build-tools/pull/5
  * remove jenkins jobs
  * remove from mirror
  * remove from github
  
* packaging to disable:
    * wazo-python-marshmallow-packaging
    * wazo-python-ldap-packaging
    * wazo-python-jaraco.functools-packaging
    * wazo-python-flask-login-packaging
    * wazo-python-cheroot-packaging
    * wazo-python-cherrypy3-packaging
    * wazo-python-werkzeug-packaging
    * xivo-python-flask-wtf-packaging (change nestbox/wazo-ui to python3-flaskext.wtf first)
    * xivo-python-flask-cors-packaging
    * xivo-python-websockets-packaging
    * xivo-consul-packaging (replaced by wazo-consul-config, because consul is now shipped by debian, wazo-consul-config just configure it and add systemd service hook for the token thing)
    * xivo-consul-cli-packaging
    
    * wazo-python-wsaccel-packaging
    * wazo-python-tempora-packaging
    * wazo-python-portend-packaging

* Remove usage of sileht/mockerserver docker image when  https://github.com/jamesdbloom/mockserver/issues/661 / https://github.com/jamesdbloom/mockserver/pull/662 is released:
    * wazo-dird
    * wazo-webhookd

* monit missing in buster repository:
  * manually copy from buster-backports to wazo-dev-buster
  * remove the copied packages when monit come back in buster main repository


TODO upgrade infra (ne doit pas impacter la migration vers buster sauf si nécessaire)

Upgrade instructions: https://www.debian.org/releases/buster/amd64/release-notes/ch-upgrading.en.html

* kvm-1-dev
* kvm-2-dev
* kvm-3-dev
* kvm-1-prod
* mirror.wazo.community
* openldap-dev.lan.wazo.io
* trafgen.lan.wazo.io (still jessie)
* perusse.lan.wazo.io (still jessie)
* webserver (provd.wazo.io)
* you (portal.wazo.community)
* mirror.lan.wazo.io
* jenkins-private



DONE:
    
    
    
    
* jenkins job issues: https://jenkins.wazo.community/view/Buster%20Failed/
    * dahdi-linux: upgrade to 3.0.0 some gcc warning tagged as error in buster https://jenkins.wazo.community/view/Buster%20Failed/job/build-package-dahdi-linux-kernel-module-buster/lastBuild/console
    * dahdi-tools: upgrade to 3.0.0 an gcc warning tagged as error in buster https://jenkins.wazo.community/job/build-package-multi-arch/872/console
    * wazo-webhookd: 
        [MA] mockserver ssl issue: https://github.com/jamesdbloom/mockserver/issues/661 / https://github.com/jamesdbloom/mockserver/pull/662
        [MA] temporary uses https://hub.docker.com/r/sileht/mockserver
    * wazo-websocketd: test_can_connect_after_rabbitmq_restart passes locally but not in Jenkins https://jenkins.wazo.community/job/integration-tests-nolock/10670/console
    * xivo-sounds: missing audio files ? https://jenkins.wazo.community/job/build-package-no-arch/8418/console
    * wazo-plugind: quelques tests ne passent pas pour des raisons encore inconnues -> besoin de plus d'investigation.
    * wazo-dird:
        [MA] some tests need to be fixed
        [MA] impacted by mockserver/openssl bug.https://github.com/jamesdbloom/mockserver/issues/661 / https://github.com/jamesdbloom/mockserver/pull/662
        [MA] temporary uses https://hub.docker.com/r/sileht/mockserver
    
* Update requirements:    
  * Script: https://github.com/sileht/wazo-buster-dep-update

* Fix tests and update marshmallow/beautifulsoup/websocketclient API:
    * pour marshmallow migration et setup job jenkins: https://zuul.wazo.community/etherpad/p/wazo-buster-help
    * [MA] xivo-lib-python
    * [MA] wazo-webhookd*
    * [MA] wazo-acceptance
    * [MA] wazo-agentd
    * [MA] wazo-agentd-client
    * [MA] wazo-agentd-cli
    * [MA] wazo-auth
    * [MA] wazo-auth-cli
    * [MA] wazo-auth-client
    * [MA] wazo-auth-keys
    * [MA] wazo-call-logd
    * [MA] wazo-call-logd-client
    * [MA] wazo-calld
    * [MA] wazo-calld-client
    * [MA] wazo-chatd
    * [MA] wazo-chatd-client
    * [MA] wazo-confd
    * [MA] wazo-confd-client
    * [MA] wazo-dird
    * [MA] wazo-dird-client
    * [MA] wazo-dird-phoned
    * [MA] wazo-market
    * [MA] wazo-market-client
    * [MA] wazo-plugind *** Revoir OptionField()
    * [MA] wazo-plugind-client
    * [MA] wazo-plugind-cli
    * [MA] wazo-provd-client
    * [MA] wazo-service
    * [MA] wazo-setupd
    * [MA] wazo-setupd-client
    * [MA] wazo-websocketd*
    * [MA] wazo-agid
    * [MA] xivo-amid
    * [MA] xivo-amid-client
    * [MA] xivo-bus
    * [MA] xivo-confgend
    * [MA] xivo-config
    * [MA] xivo-fetchfw
    * [MA] wazo-uuid
    * [MA] xivo-manage-db
    * [MA] wazo-provd
    * [MA] xivo-stat
    * [MA] xivo-sysconfd
    * [MA] xivo-tools
    * [MA] xivo-manage-db
    * [MA] xivo-dao
    * [MA] xivo-lib-rest-client
    * [MA] xivo-test-helpers
    
* update xivo-build-tools images:
    * long GPG keys
    * jenkins job buster
    * new docker image
    
* Jenkins: job upgrade to buster
* [MA] wazo-dist-upgrade stretch to buster
* upgrade Postgres 9.6 to 11
  * Create wazo-migrate-db-96-to-11
* Documentation
  * sed s/stretch/buster/
  * upgrade procedure
  * upgrade archive procedures
  * link buster changes https://wiki.debian.org/NewInBuster
  * link buster changes https://www.debian.org/releases/buster/amd64/release-notes/ch-whats-new.en.html
  * summary buster changes to dev@wazo.io
* New Debian distributions: wazo-dev-buster, wazo-rc-buster, pelican-buster
* import monit in wazo-dev-buster
* trace unmerged branches
* packaging:
    * wazo-python-asynqp-packaging 0.6
* ISO install buster
* wazo-dist pelican-buster = works
* Zuul: create debian 10 image https://github.com/wazo-pbx/sf-config/pull/17
* Jenkins: job install via script on buster (daily-wazo-rolling-dev does exactly that)
* Ansible playbook public
* acceptance tests

MERGE

* rebase all buster branches
* restore requirements.txt to master.zip
* change default distribution in package build
* merge all buster branches


* check all packages in wazo-dev-buster have been built after 2019-09-03 (included)
* grep git+https: in all requirements

[SD] * Rename xivo-dist package
  * wazo-upgrade
  * wazo-doc
  * wazo-dist-upgrade
  * wazo-ansible
* Rename xivo-upgrade package (https://github.com/wazo-platform/xivo-upgrade/pull/25)
* Split wazo-dist-upgrade
* Upgrade tests pass
* Acceptance tests pass


Release blockers

* [SD] grep 9.6 (postgres) https://zuul.wazo.community/etherpad/p/buster-9.6
* grep stretch in all repos https://zuul.wazo.community/etherpad/p/buster-stretch
* grep phoenix in all repos
* Dockerfiles
  * debian:buster
  * python:2
  * python:3
  * postgres
  * rabbitmq
  * nginx?
  * others?
* check errors/warnings in logs:
    * package builder
    * upgrade
    * iso install
    * /var/log/wazo*
    * /var/log/apparmor
* xivo-load to buster & check load-monitor and logs

* review wazo-doc PR: https://github.com/wazo-platform/wazo-doc/pulls
* use httpx for push mobile apple: https://github.com/wazo-platform/wazo-webhookd/pull/47
* ISO PR: https://github.com/wazo-platform/wazo-iso/pull/8
* check that https://github.com/wazo-platform/wazo-dist-upgrade/pull/1 fixes the problem

WAZO-TEST

* check /etc/**/*.dpkg.*
* manual tests

POST TESTS

* backport to pelican-stretch from wazo-dev-stretch:
    xivo-dist
    xivo-upgrade
    wazo-dist-upgrade
    
* backport to phoenix-stretch from wazo-dev-stretch:
    xivo-upgrade
    wazo-dist-upgrade
    
* update install scripts for pelican-buster

* Ansible playbook private https://github.com/TinxHQ/wazo-ansible-private/tree/buster

* use nftables instead of iptables: https://www.debian.org/releases/buster/amd64/release-notes/ch-whats-new.en.html#nftables
  (sileht): Not really urgent, buster iptables command line will stay for long and creates nftables rules instead of iptables rules inside the kernel
* disable apparmor? add apparmor config?


* zuul
  * https://github.com/wazo-platform/wazo-dird-client/pull/4
  * https://github.com/wazo-platform/wazo-ui/pull/7
  * https://github.com/wazo-platform/wazo-dird/pull/16
  * https://github.com/wazo-platform/wazo-call-logd/pull/19
  
* re-evaluate daily-upgrade coverage

