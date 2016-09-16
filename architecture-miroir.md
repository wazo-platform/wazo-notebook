Architecture technique
----------------------

Les nouveaux miroirs sont disponible sur **mirror.xivo.io**. La solution est composé :

-   reprepro : pour la gestion des miroirs
-   nginx : pour la partie serveur http

### reprepro

Toute la configuration de reprepro est disponible dans le répertoire **/data/reprepro**.

Un répertoire de gestion de miroir doit contenir les répertoires suivant :

`[mirror:repository]tree -d -L 1`
`.`
`├── conf`
`├── db`
`├── dists`
`├── incoming`
`├── lists`
`└── pool`

-   conf : contient les fichiers de configuration pour le miroir.
-   db : les fichiers de bdb.
-   dist : contient les fichiers de description de chaque distribution, ainsi que les fichiers Release.gpg.
-   incoming : le répertoire contenant les packages en attente de publication.
-   lists : contient la liste des packages par distribution et par architecture.
-   pool contient l'ensemble des packages disponible sur le miroir.

3 miroirs sont disponibles sur l'archi, voici la structure du rep **/data/reprepro** :

`[mirror:reprepro]tree -d -L 1`
`.`
`├── archive`
`├── keys`
`├── people`
`└── xivo`

-   archive : contient les packages pour les anciennes versions de xivo.
-   keys : contient les clés permettant d'authentifier le miroir.
-   people : contient des packages pour des clients, des dev.
-   xivo : l'archive principale du projet.

#### configuration

Toute la configuration d'un miroir se trouve dans le répertoire configuration, voici sa structure :

`[mirror:xivo]tree conf `
`conf`
`├── distributions`
`├── incoming`
`├── options`
`├── updates`
`└── uploaders`

-   distributions : contient la configuration de chaque distribution, voici un exemple de configuration, les points importants sont commentés :

`Origin: proformatique.com`
`# description de la suite`
`Label: lenny-xivo-gallifrey`
`Suite: lenny-xivo-gallifrey`
`Codename: lenny-xivo-gallifrey`
`# les différentes archi disponibles`
`Architectures: i386 source`
`# les composants disponible`
`Components: main non-free`
`# le miroir sur lequel se synchroniser (cf update dans le même paragraphe)`
`Update: lenny-xivo-gallifrey-rc`
`# on peut préciser que l'on veut synchroniser une suite sur plusieurs miroirs de  la manière suivante :`
`# Update: lenny-xivo-gallifrey-farm-main lenny-xivo-gallifrey-farm-non-free, il devra y avoir deux déclarations dans le fichier update`
`Description: Archive lenny-xivo-gallifrey`
`# avec quelle clé signer les paquets (indispensable pour que apt ne râle pas)`
`SignWith: 9193E98C`

-   incoming : configuration du répertoire dans lequel les nouveaux packages seront stockés avant validation (cf upload de paquet plus bas) :

`Name: lenny-xivo-gallifrey`
`IncomingDir: incoming/lenny-xivo-gallifrey`
`TempDir: /tmp`
`Allow: lenny-xivo-gallifrey`
`Default: lenny-xivo-gallifrey`
`Cleanup: on_deny on_error`

-   options : les options globales de configuration :

`verbose`
`basedir /data/reprepro/xivo`
`ignore undefinedtarget`

-   update : ce fichier est important. C'est en effet ici que nous allons définir comment se synchroniser sur un miroir distant ou local :

`Name: lenny-xivo-gallifrey-rc`
`Method: `[`http://mirror.xivo.io/debian/`](http://mirror.xivo.io/debian/)
`Suite: lenny-xivo-gallifrey-rc`
`Components: main non-free`
`Architectures: i386 source`
`VerifyRelease: B33A50859193E98C`

-   uploaders : les personnes autorisées a publier des paquets sur le miroir (en utilisant dput par exemple) :

`allow * by key 780450F7`
`allow * by key 4EFADA39`
`allow * by key FB075CEF`

#### reprepro cheat sheet

-   Si reprepro exécuté en dehors du répertoire miroir (ici /data/reprepro/xivo) : reprepro -vb /data/reprepro/xivo <action>
-   Lister quelle distribution inclut ce paquet : reprepro ls <package>
-   Lister les paquets inclus dans cette distribution : reprepro list <distribution>
-   Ajouter un paquet à une distribution : reprepro includedeb <distribution> package.deb
-   Ajouter des paquets uploadés avec dput : reprepro processincoming <distribution>
-   Copier un paquet d'une distribution à l'autre : reprepro copy destination\_dist source\_dist <package>
-   Retirer un paquet d'une distribution : reprepro remove <distribution> <package>
-   Supprimer une distribution : Éditer conf/distributions puis reprepro --delete clearvanished

