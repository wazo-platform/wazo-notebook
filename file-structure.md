# Wazo daemon file structure

## Typical file structure for daemon source code

Note: replace "daemon" with your daemon name

- [ ] AUTHORS: Contains the list of contributors. Use `Wazo Communication Inc.` if you are part of Wazo core team.
- [ ] requirements.txt: Use .zip archives provided by Github for Git dependencies
- [ ] test-requirements.txt: Use .zip archives provided by Github for Git dependencies
- [ ] bin/: No daemon runners in there, use setup.py:console_scripts instead
- [ ] templates/: templates that Wazo admins can tweak for their needs.
- [ ] wazo_daemon/
  - [ ] main.py: The main() function that loads configuration and starts the controller (among other things)
  - [ ] config.py: Everything related to daemon configuration
  - [ ] controller.py: Prepares, starts and stops threads and objects
  - [ ] http_server.py: The WSGI server listening for HTTP(S) requests
  - [ ] http.py: API endpoints of the daemon (not plugins) and HTTP routines shared with plugins
  - [ ] api.yml: OpenAPI specification for API endpoints of the daemon (not plugins)
  - [ ] schemas.py: Schemas used for API endpoints
  - [ ] services.py: Services that process API requests
  - [ ] exceptions.py: All exceptions used in the daemon (not plugins)
  - [ ] service_discovery.py: self-checking function
  - [ ] bus.py: Bus consumer / publisher
  - [ ] plugins/: One directory by plugin. If multiple kinds of plugins: plugins_view / plugins_service / plugins_backend
    - [ ] plugin.py
    - [ ] http.py
    - [ ] schemas.py
    - [ ] services.py
    - [ ] queries.py
    - [ ] api.yml
  - [ ] plugin_helpers/: Code that is shared among plugins (but not the rest of the daemon)
    - [ ] exceptions: Exceptions shared among plugins
  - [ ] database/
    - [ ] models.py: make a directory if necessary
    - [ ] queries.py: make a directory if necessary
  - [ ] templates/: Templates that are internal to the daemon, which Wazo admins should not have to modify.

## Typical file structure for daemon integration tests

- [X] Makefile
- [ ] docker
  - [ ] Dockerfile-*
- [ ] assets/
  - [X] docker-compose.yml: leave the commented mount points for dependencies, for manual edition
  - [X] docker-compose.*.override.yml: version=3
  - [ ] ssl/
    - [ ] README.md
    - [ ] <daemon>/
      - [ ] openssl.conf
      - [ ] server.crt
  - [ ] daemon_data/
  - [ ] etc/daemon/
- [ ] suite/
  - [X] helpers/
    - [ ] base.py
    - [ ] fixtures.py
- [ ] test-requirements.txt: Use .zip archives provided by Github for Git dependencies
