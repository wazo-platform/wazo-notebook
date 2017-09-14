# Arborescence typique pour un plugin REST API

- [ ] user/
  - [ ] plugin.py
  - [ ] http.py
  - [ ] schemas.py
  - [ ] services.py
  - [ ] queries.py
  - [ ] api.yml

# Arborescence typique pour un démon

- [ ] requirements.txt: pour les dépendances Git, utiliser les .zip
- [ ] test-requirements.txt: pour les dépendances Git, utiliser les .zip
- [ ] bin/: ne pas mettre de lanceur, utiliser setup.py:console_scripts
- [ ] templates/: les templates qui peuvent servir pour les administrateurs
- [ ] wazo_daemon/
  - [ ] main.py: la fonction main() qui charge la config et lance le controller (entre autres)
  - [ ] config.py: tout ce qui a trait à la configuration du démon
  - [ ] controller.py: initialise, démarre et arrête les threads/objets
  - [ ] http_server.py: le serveur WSGI qui écoute en HTTP(S)
  - [ ] http.py: les routes du démon et comportements HTTP partagés par les plugins
  - [ ] api.yml: la spec des routes HTTP
  - [ ] schemas.py: les schemas des routes HTTP
  - [ ] services.py: les services des routes HTTP
  - [ ] exceptions.py: les exceptions du démon, pas utilisées par les plugins
  - [ ] service_discovery.py: la fonction de self-check
  - [ ] bus.py: publisher et/ou consumer du bus
  - [ ] plugins/: un répertoire par plugin. Si plusieurs sortes de plugins: plugins_view / plugins_service / plugins_backend
  - [ ] plugin_helpers/: tout le code partagé par plusieurs plugins (mais pas par le reste)
    - [ ] exceptions: les exceptions partagées par les plugins
  - [ ] database/
    - [ ] models.py (répertoire si nécessaire)
    - [ ] queries.py (répertoire si nécessaire)
  - [ ] templates/: les templates qui ne servent qu'au démon et qui n'ont pas vocation à être utilisés par les administrateurs
  
# Arboresence typique des tests d'intégration

- [X] Makefile
- [ ] Dockerfile-*
- [ ] assets/
  - [ ] my-asset/
    - [X] docker-compose.yml: laisser les mount point pour les dépendances commentés
- [ ] suite/
  - [ ] helpers/
    - [ ] base.py
    - [ ] fixtures.py
- [ ] test-requirements.txt: pour les dépendances Git, utiliser les .zip
