# Repos

General rule: one repo per Debian package

## Conventions

- xivo-*: older repositories. Will be renamed to wazo-* eventually.
- wazo-*: newer repositories
  - wazo-admin-ui-*: plugins for wazo-admin-ui, the new web interface for Wazo
- debian-repo-*: Debian mirror configuration (for reprepro)
- asterisk-*: Variants of Asterisk package (debug, without patches, etc.)

- *-packaging: Debian packaging repos, for libraries/software not yet packaged by Debian
- *-client: Python libraries for using REST API, e.g. xivo-confd-client is a library for the REST API provided by the daemon xivo-confd
- *-cli: CLI tools for using REST API, e.g. xivo-agentd-cli is a CLI tool for interacting with the REST API provided by the daemon xivo-agentd. The CLI tools use the *-client library.
- others: forks, older packaging repos, misc tools

## Not-packaged repos

### Public-oriented repos

- sphinx-git: Forked Python library to integrate Git logs inside Sphinx-generated docs, used for http://documentation.wazo.community/en/stable/changelog.html#changelog
- wazo-doc-api: Wazo REST API documentation exposed on http://developers.wazo.io/ (ReDoc)
- wazo-js-sdk: Library for Javascript applications using Wazo REST APIs.
- wazo-logo: Collection of Wazo logos
- wazo-notebook: Collection of text files for documentation too specific to be written in xivo-doc
- wazo-pbx.github.io: Website exposed on http://wazo.community
- wazo-react-components: React.JS components that can be used in Javascript applications
- xivo-blog: Blog exposed on http://blog.wazo.community
- xivo-doc: Documentation exposed on http://documentation.wazo.community
- xivo-migration-scripts: Wazo install scripts exposed on http://mirror.wazo.community/fai/xivo-migration
- xivo-presentations: Collection of presentations about Wazo
- xivo-ws: Python library to interact with the deprecated Wazo WebServices

### Development

- debian-add-archive: Tool for adding new archive Debian repo
- debian-pxelinux: Configuration for installing Wazo via PXE server
- denv: Tool for working with Wazo integration tests
- kvm: Tool for deploying Wazo servers on KVM hypervisors
- lordboard: Web interface reporting tests executed in a Testlink test plan
- wazo-libtestlink: Python library for interacting with Testlink
- wazo-market: Database of Wazo plugins (different from provisioning plugins, see xivo-provd-plugins)
- wazo-sdk: Tools for developers
- xgong: Tool for interconnecting Jenkins with Asterisk (e.g. with an intercom)
- xivo-build-tools: Builder for Debian packages
- xivo-ci: Tools used by Jenkins (CI: Continuous Integration)
- xivo-experimental: Collection of experimental tools
- xivo-install-cd: Code for building the ISO image of Wazo
- xivo-pjsip: Documentation for using PJSIP (the latest Asterisk SIP channel) with Wazo
- xivo-tools: Collection of specific tools for Wazo

### Tests

- asterisk-lab: Module for Asterisk introducing testing features
- chan-test: Simple Asterisk channel used for testing purposes
- debian-installer: Files for automatic Debian installer (FAI: Fully Automated Installer)
- mockserver-client-python: Forked Python library to interact with Mockserver in integration tests
- pylinphonelib: Python library for interacting with Linphone (CLI)
- sccp-client: Library for interacting with Asterisk SCCP channel
- sccpp: Call-spawner for Asterisk SCCP channel
- wazo-terraform: Tests using Terraform to deploy Wazo servers
- xivo-acceptance: Automated acceptance tests for Wazo
- xivo-benchmark: Benchmarking tests
- xivo-load-monitor: Load-tests monitor interface
- xivo-load-tester: Tests scenarios for load testing
- xivo-test-helpers: Python library used by integration tests
