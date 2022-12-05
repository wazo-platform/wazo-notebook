# Repos

General rule: one repo per Debian package

## Conventions

- `xivo-*`: older repositories. Will be renamed to `wazo-*` eventually.
- `wazo-*`: newer repositories
- `debian-repo-*`: Debian mirror configuration (for reprepro)
- `asterisk-*`: Variants of Asterisk package (debug, without patches, etc.)

- `*-packaging`: Debian packaging repos, for libraries/software not yet packaged by Debian
- `*-client`: Python libraries for using REST API, e.g. wazo-confd-client is a library for the REST API provided by the daemon wazo-confd
- `*-cli`: CLI tools for using REST API, e.g. wazo-agentd-cli is a CLI tool for interacting with the REST API provided by the daemon wazo-agentd. The CLI tools use the `*-client` library.
- others: forks, older packaging repos, misc tools

## Repos that are not Debian-packaged

### Public-oriented repos

- [wazo-doc-api](https://github.com/wazo-platform/wazo-doc-api): Wazo REST API documentation exposed on http://developers.wazo.io/ (ReDoc)
- [wazo-js-sdk](https://github.com/wazo-platform/wazo-js-sdk): Library for Javascript applications using Wazo REST APIs.
- [wazo-logo](https://github.com/wazo-platform/wazo-logo): Collection of Wazo logos
- [wazo-notebook](https://github.com/wazo-platform/wazo-notebook): Collection of text files for documentation too specific to be written in wazo-platform.org
- [wazo-platform.org](https://github.com/wazo-platform/wazo-platform.org): Website exposed on http://www.wazo-platform.org

### Development

- [debian-add-archive](https://github.com/wazo-platform/debian-add-archive): Tool for adding new archive Debian repo
- [debian-pxelinux](https://github.com/wazo-platform/debian-pxelinux): Configuration for installing Wazo via PXE server
- [denv](https://github.com/wazo-platform/denv): Tool for working with Wazo integration tests
- [kvm](https://github.com/wazo-platform/kvm): Tool for deploying Wazo servers on KVM hypervisors
- [lordboard](https://github.com/wazo-platform/lordboard): Web interface reporting tests executed in a Testlink test plan
- [wazo-libtestlink](https://github.com/wazo-platform/wazo-libtestlink): Python library for interacting with Testlink
- [wazo-market](https://github.com/wazo-platform/wazo-market): Database of Wazo plugins (different from provisioning plugins, see wazo-provd-plugins)
- [wazo-sdk](https://github.com/wazo-platform/wazo-sdk): Tools for developers
- [xgong](https://github.com/wazo-platform/xgong): Tool for interconnecting Jenkins with Asterisk (e.g. with an intercom)
- [xivo-build-tools](https://github.com/wazo-platform/xivo-build-tools): Builder for Debian packages
- [xivo-ci](https://github.com/wazo-platform/xivo-ci): Tools used by Jenkins (CI: Continuous Integration)
- [xivo-install-cd](https://github.com/wazo-platform/xivo-install-cd): Code for building the ISO image of Wazo
- [wazo-tools](https://github.com/wazo-platform/wazo-tools): Collection of specific tools for Wazo

### Tests

- [chan-test](https://github.com/wazo-platform/chan-test): Simple Asterisk channel used for testing purposes
- [debian-installer](https://github.com/wazo-platform/debian-installer): Files for automatic Debian installer (FAI: Fully Automated Installer)
- [mockserver-client-python](https://github.com/wazo-platform/mockserver-client-python): Forked Python library to interact with Mockserver in integration tests
- [pylinphonelib](https://github.com/wazo-platform/pylinphonelib): Python library for interacting with Linphone (CLI)
- [sccp-client](https://github.com/wazo-platform/sccp-client): Library for interacting with Asterisk SCCP channel
- [sccpp](https://github.com/wazo-platform/sccpp): Call-spawner for Asterisk SCCP channel
- [wazo-terraform](https://github.com/wazo-platform/wazo-terraform): Tests using Terraform to deploy Wazo servers
- [wazo-acceptance](https://github.com/wazo-platform/wazo-acceptance): Automated acceptance tests for Wazo
- [xivo-benchmark](https://github.com/wazo-platform/xivo-benchmark): Benchmarking tests
- [xivo-load-monitor](https://github.com/wazo-platform/xivo-load-monitor): Load-tests monitor interface
- [xivo-load-tester](https://github.com/wazo-platform/xivo-load-tester): Tests scenarios for load testing
- [wazo-test-helpers](https://github.com/wazo-platform/wazo-test-helpers): Python library used by integration tests
