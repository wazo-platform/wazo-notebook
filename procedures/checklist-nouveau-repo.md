- Créer le repo sur Github
- Ajouter le hook Github: Jenkins Git vers <https://jenkins.wazo.community>

OU

- Rouler le script xivo-tools/dev-tools/new-repo

PUIS

- Ajouter le repo dans xivo-build-tools/etc/packages
- Ajouter le repo dans xivo-tools/dev-tools/repos si ce n'est pas un repo \*-packaging
- Ajouter le job sur Jenkins
- Ajouter le fichier de config Travis, cela activera le build Travis automatiquement
