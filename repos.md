# Repos

General rule: one repo per Debian package

## Conventions

- `xivo-*`: older repositories. Will be renamed to `wazo-*` eventually.
- `wazo-*`: newer repositories
  - `wazo-admin-ui-*`: plugins for wazo-admin-ui, the new web interface for Wazo
- `debian-repo-*`: Debian mirror configuration (for reprepro)
- `asterisk-*`: Variants of Asterisk package (debug, without patches, etc.)

- `*-packaging`: Debian packaging repos, for libraries/software not yet packaged by Debian
- `*-client`: Python libraries for using REST API, e.g. xivo-confd-client is a library for the REST API provided by the daemon xivo-confd
- `*-cli`: CLI tools for using REST API, e.g. xivo-agentd-cli is a CLI tool for interacting with the REST API provided by the daemon xivo-agentd. The CLI tools use the `*-client` library.
- others: forks, older packaging repos, misc tools

## Not-packaged repos

### Public-oriented repos

- [sphinx-git](https://github.com/wazo-pbx/sphinx-git): Forked Python library to integrate Git logs inside Sphinx-generated docs, used for http://documentation.wazo.community/en/stable/changelog.html#changelog
- [wazo-doc-api](https://github.com/wazo-pbx/wazo-doc-api): Wazo REST API documentation exposed on http://developers.wazo.io/ (ReDoc)
- [wazo-js-sdk](https://github.com/wazo-pbx/wazo-js-sdk): Library for Javascript applications using Wazo REST APIs.
- [wazo-logo](https://github.com/wazo-pbx/wazo-logo): Collection of Wazo logos
- [wazo-notebook](https://github.com/wazo-pbx/wazo-notebook): Collection of text files for documentation too specific to be written in xivo-doc
- [wazo-pbx.github.io](https://github.com/wazo-pbx/wazo-pbx.github.io): Website exposed on http://wazo.community
- [wazo-react-components](https://github.com/wazo-pbx/wazo-react-components): React.JS components that can be used in Javascript applications
- [xivo-blog](https://github.com/wazo-pbx/xivo-blog): Blog exposed on http://blog.wazo.community
- [xivo-doc](https://github.com/wazo-pbx/xivo-doc): Documentation exposed on http://documentation.wazo.community
- [xivo-migration-scripts](https://github.com/wazo-pbx/xivo-migration-scripts): Wazo install scripts exposed on http://mirror.wazo.community/fai/xivo-migration
- [xivo-presentations](https://github.com/wazo-pbx/xivo-presentations): Collection of presentations about Wazo
- [xivo-ws](https://github.com/wazo-pbx/xivo-ws): Python library to interact with the deprecated Wazo WebServices

### Development

- [debian-add-archive](https://github.com/wazo-pbx/debian-add-archive): Tool for adding new archive Debian repo
- [debian-pxelinux](https://github.com/wazo-pbx/debian-pxelinux): Configuration for installing Wazo via PXE server
- [denv](https://github.com/wazo-pbx/denv): Tool for working with Wazo integration tests
- [kvm](https://github.com/wazo-pbx/kvm): Tool for deploying Wazo servers on KVM hypervisors
- [lordboard](https://github.com/wazo-pbx/lordboard): Web interface reporting tests executed in a Testlink test plan
- [wazo-libtestlink](https://github.com/wazo-pbx/wazo-libtestlink): Python library for interacting with Testlink
- [wazo-market](https://github.com/wazo-pbx/wazo-market): Database of Wazo plugins (different from provisioning plugins, see xivo-provd-plugins)
- [wazo-sdk](https://github.com/wazo-pbx/wazo-sdk): Tools for developers
- [xgong](https://github.com/wazo-pbx/xgong): Tool for interconnecting Jenkins with Asterisk (e.g. with an intercom)
- [xivo-build-tools](https://github.com/wazo-pbx/xivo-build-tools): Builder for Debian packages
- [xivo-ci](https://github.com/wazo-pbx/xivo-ci): Tools used by Jenkins (CI: Continuous Integration)
- [xivo-experimental](https://github.com/wazo-pbx/xivo-experimental): Collection of experimental tools
- [xivo-install-cd](https://github.com/wazo-pbx/xivo-install-cd): Code for building the ISO image of Wazo
- [xivo-pjsip](https://github.com/wazo-pbx/xivo-pjsip): Documentation for using PJSIP (the latest Asterisk SIP channel) with Wazo
- [xivo-tools](https://github.com/wazo-pbx/xivo-tools): Collection of specific tools for Wazo

### Tests

- [asterisk-lab](https://github.com/wazo-pbx/asterisk-lab): Module for Asterisk introducing testing features
- [chan-test](https://github.com/wazo-pbx/chan-test): Simple Asterisk channel used for testing purposes
- [debian-installer](https://github.com/wazo-pbx/debian-installer): Files for automatic Debian installer (FAI: Fully Automated Installer)
- [mockserver-client-python](https://github.com/wazo-pbx/mockserver-client-python): Forked Python library to interact with Mockserver in integration tests
- [pylinphonelib](https://github.com/wazo-pbx/pylinphonelib): Python library for interacting with Linphone (CLI)
- [sccp-client](https://github.com/wazo-pbx/sccp-client): Library for interacting with Asterisk SCCP channel
- [sccpp](https://github.com/wazo-pbx/sccpp): Call-spawner for Asterisk SCCP channel
- [wazo-terraform](https://github.com/wazo-pbx/wazo-terraform): Tests using Terraform to deploy Wazo servers
- [xivo-acceptance](https://github.com/wazo-pbx/xivo-acceptance): Automated acceptance tests for Wazo
- [xivo-benchmark](https://github.com/wazo-pbx/xivo-benchmark): Benchmarking tests
- [xivo-load-monitor](https://github.com/wazo-pbx/xivo-load-monitor): Load-tests monitor interface
- [xivo-load-tester](https://github.com/wazo-pbx/xivo-load-tester): Tests scenarios for load testing
- [xivo-test-helpers](https://github.com/wazo-pbx/xivo-test-helpers): Python library used by integration tests
