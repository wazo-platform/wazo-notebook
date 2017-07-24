# Arborescence typique pour un plugin REST API

user/
- plugin.py
  - class Plugin
- resource.py
  - class UserResource
- schema.py
  - class UserSchema
- service.py
  - class UserService
- api.yml

# Arborescence typique pour un démon

wazo_daemon/
- config.py
- core
  - plugin_manager.py
  - rest_api.py
  - database
    - models.py
