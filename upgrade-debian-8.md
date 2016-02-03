XiVO - Migration Debian 7 (wheezy) vers 8 (jessie)
==================================================

-   Master ticket: <http://projects.xivo.io/issues/5910>
-   Debian:
    -   Release info: <https://www.debian.org/releases/jessie/>
    -   Release notes: <https://www.debian.org/releases/jessie/releasenotes>

TODO
----

-   avoir des builders amd64 et i386 sur jessie
    -   renommer builder-wheezy en builder-32
    -   renommer builder-wheezy en builder-wheezy-64
    -   mettre a jour le DNS avec les nouveaux noms, etc
    -   faire un snapshot des builder en wheezy
    -   faire l'upgrade

-   reconstruire certains paquets sur jessie (principalement les trucs en C)
    -   reconstruire tous les paquets xivo-\*

-   s'assurer que le paquet 'dahdi-linux-modules-\*' est bien builder
-   modifier xivo-upgrade pour upgrade de wheezy (13.25 - 15.19) vers jessie
    -   traiter le cas d'un upgrade 14.17 ou avant, qui échoue actuellement a cause qu'il essaie d'installer xivo-dist "jessie" (depends python \>= 2.7.5, ce qui fait planter le truc)

-   modifier xivo-upgrade pour upgrader de squeeze (13.24 ou avant) vers jessie (ultimement)
    -   demande du service: pouvoir faire un xivo-upgrade d'une version de XiVO vers la "derniere de version de XiVO sous Debian Wheezy"
        -   idéalement, faire un "xivo-upgrade" a partir d'une 13.23 fait un upgrade vers 15.19, qui après un reboot est une 15.19 "qui fonctionne bien" (i.e. avec un xivo-service qui match la version). Le but est de pouvoir étaler une migration squeeze -\> wheezy -\> jessie en deux fois
        -   idéalement, ca serait bien que xivo-upgrade -d fonctionne lorsqu'on change de version Debian
    -   Faire un test de 13.23 a 15.19 (archive) Pour valider que la doc est toujours bonne

-   migrer toutes les images docker de wheezy vers jessie
-   mettre a jour les différentes méthodes d'installations
    -   PXE
        -   modifier le script de génération des entrées PXE d'archive pour utiliser jessie
        -   modifier le script de génération des entrées PXE d'archive pour avoir une entrée raid software
        -   pouvoir installer une Debian jessie vanille
        -   s'assurer que c'est possible d'installer un xivo 15.20 en jessie
    -   ISO
    -   script d'installation

-   regarder que les tests automatique d'upgrade fonctionnent toujours
    -   reactiver la job upgrade\_meta

-   mettre a jour la webi...
    -   probleme avec le retour des references
    -   probleme lors de la sauvegarde d'une touche de fonction custom
    -   probleme sur la page des certificats
    -   probleme sur la page Services / CTI Server / General
    -   probleme sur la page des plugins, apres en avoir installé un la description n'est pas correcte.
    -   virer aussi les paquets du miroir libjs

-   postgresql 9.1/9.0 vers 9.4, s'assurer que suite a l'upgrade, postgresql marche toujours bien
-   faire le menage dans nos paquets backportés/custom
-   jenkins: mettre a jour le job install-daily\_xivo\_script (part d'un snapshot wheezy)
-   verifier que, lors de l'upgrade et l'installation openssh-server en jessie, que le "PermitRootPassword" conserve une valeur qui ne vas pas faire bloquer ceux qui se connecte sur leur xivo en root via ssh en utilisant un mot de passe
    -   <https://www.debian.org/releases/jessie/i386/release-notes/ch-information.en.html#openssh>

-   tester que fail2ban fonctionne toujours bien, voir <https://github.com/fail2ban/fail2ban/blob/master/ChangeLog>
-   verifier les dernières références à wheezy dans tout xivo

-   rajouter des upgrade notes
    -   dire quels paquets debian ont dégagé (ca ne devrait pas causer de probleme, mais si jamais qqun en dépendait)
    -   donner la procédure lorsque la version de XiVO \<= 13.24
    -   reference vers release notes debian jessie
        -   mentionner qu'il ne faut pas avoir les wheezy-backports dans son source.list
    -   utilisation de halt vs shutdown/poweroff
    -   un mot sur bootlogd, i.e. journalctl au lieu de /var/log/boot
    -   dire que ca prend jessie \*avec systemd\*
    -   postgresql 9.1 vers 9.4
    -   parler des quelques petites différences avec jessie
        -   lors du boot, on voit le tty avant que le systeme ait fini de booter
        -   si on arrete/reboot, bien souvent la connection ssh reste ouverte, pour fermer utiliser \~.
    -   systemd related change
        -   généralités: ne pas utiliser /etc/init.d, on utilise des unit files, etc
        -   xivo-ctid ami-proxy, configuration has changed (upgrade automatique)
        -   /etc/default/asterisk, si vous avez des modifications (autre que confd), vous devez les porter

-   penser au probleme de Seb, i.e. avec une ligne "deb wheezy-backports", et un "apt-get update" avec un probleme réseau, résultat: upgrade qui foire
-   Enlever le patch requests (2.0.0) dans xivo-python-swaggerpy-packaging
-   Verifier la compilation du xivoclient
-   verifier que wheezy-backports n'est installé automatiquement sur une install fraiche (si oui alors mettre a jour l'url de wheezy-backports)
-   Modifier le message d'upgrade squeeze-\>jessie pour dire que c'est un état intermédiaire (15.19) et un autre xivo-upgrade une fois redémarré pour completer
-   Mettre un autre test dans xivo-upgrade pour s'avoir si le proc accepte pae ou non
-   modifier la facon dont le hostname est mis à jour xivo-sysconfd (/etc/init.d/hostname.sh ne marche pas sous systemd -- utiliser soit hostnamectl ou hostname)
    -   en fait ca marche probablement encore, mais il y a qqch de louche
-   faire des tests manuels (?) (HA)
-   db5.1-util (et libdb5.1 et python2.6), est-ce qu'il y d'autres installations qui ont db5.1-util d'installée en non-auto, et donc avec l'état un peu étrange ?
-   regarder pourquoi parfois, après une installation fraiche puis un wizard de passer, xivo-ctid ne démarre pas correctement lors d'un reboot
-   pour install iso (xivo-install-cd) et pxe (debian-installer), qu'est-ce qu'on doit faire de /etc/default/xivo ? le virer ou le mettre à jour ?
-   consul, lorsqu'on l'arrête, systemctl le voit comme failed ?

Lors du passage en rc
---------------------

-   enlever tous les paquets du mirroir qui ont été enlevé de xivo-dev
    -   faire un diff entre la sortie de "reprepro list xivo-dev" et "reprepro list xivo-rc"
-   modifier l'entrée pxe pour utiliser jessie (debian-pxelinux branche jessie-rc) + test install

Lors du passage en prod
-----------------------

-   enlever tous les paquets du mirroir qui ont été enlevé de xivo-rc
    -   faire un diff entre la sortie de "reprepro list xivo-rc" et "reprepro list xivo-five"
-   xivo-migration-scripts: s'assurer que xivo\_install\_current pointe vers jessie
    -   faire un "git mv xivo\_install\_jessie.sh xivo\_install.sh" (i.e. pas besoin de conserver le install "wheezy")
-   merger la branche jessie-prod du dépôt debian-pxelinux + test install xivo-prod raid logiciel
-   vérifier les entrée PXE pour l'installation d'archive avec raid logiciel
-   virer le dépot git xivo-lib-js, la job jenkins et packaging qu'on ne se sert plus
-   virer les dépôts git "babel" et "backport-ssl-matchhostname" "packaging" git et leurs jobs jenkins
-   enlever la ligne en commentaire dans jenkins : daily-xivo-script pour le remettre sur current
-   demander à Sylvain si on peut virer le paquet debian "consulate" (et la job jenkins qu'on a désactivé et le dépôt git -- semble faire la meme chose que python-consul)

Optionnel/moins prioritaire
---------------------------

-   créer un unit file pour xivo-webi (et enlever les références /etc/init.d et /etc/default)
-   mettre a jour les autres machines de notre infra
    -   kvm-1-dev
    -   kvm-2-dev
    -   kvm-3-dev
    -   trafgen
        -   mettre à jour le code de load-monitor...
    -   openldap-dev
-   Supprimer packet xivo-extra-packaging (C'est quoi ?)
-   Enlever commentaire ssl dans lib-python: xivo/http\_helper
-   cleaner un peu debian-installer ? entre autres références à atftp et dhcp3-server, etc
-   retravailler le postinst de xivo-config (références a /etc/init.d + créer unit file pour spawn-fcgi ? ou utiliser qqch d'autre?)

Notes d'upgrade
---------------

### Procédure d'upgrade wheezy vers jessie

#### pre-upgrade

-   faire apt-get update
-   faire un "apt-get dist-upgrade" pour etre sur la dernière version de wheezy...
-   review pending actions in aptitude
    -   lancer "aptitude", appuyer sur g, reviewer ce qu'il dit; si ca fait pas de sens, quitter, puis faire un "aptitude keep-all" pour "cancels all scheduled actions on all packages"
-   checking packages status
    -   lancer "dpkg --audit"
    -   lancer "dpkg --get-selections" et regarder que tous les paquets sont en status "install"... (pas de paquet dans le status hold)
    -   purger les paquets qui sont removed; pour obtenir la liste: dpkg -l | awk '/\^rc/ { print \$2 }'
    -   lancer "aptitude search '\~ahold' "
-   cleaner le reste du cruft...
    -   aptitude search ?obsolete
    -   apt-get autoremove --purge
    -   find /etc -name '\*.dpkg-old' -o -name '\*.dpkg-new' -o -name '\*.dpkg-dist'
-   apt-get autoclean
-   s'assurer qu'il a assez de place pour l'upgrade

#### upgrade

-   changer wheezy par jessie dans sources.list
    -   ne pas utiliser le backport jessie lors de l'upgrade (enfin, je sais pas ce que ca fait mais -- le remettre apres si utile)
-   sur nos machines ici, peut rajouter la ligne "Acquire::<http::Proxy> "<http://mirror.lan-quebec.avencall.com:3142>";" dans /etc/apt/apt.conf pour accélérer l'upgrade
-   apt-get update
-   apt-get upgrade
-   apt-get dist-upgrade

#### post-upgrade

-   apt-get autoremove --purge
-   vérifier qu'on a le meta package de linux-image
-   refaire un autre purge des paquets removed
-   virer acpid (remplacer par la partie logind de systemd)
-   rebooter
-   virer l'ancienne image kernel
-   faire le ménage dans les paquets "dummy" ou "obsolete" (dpkg -l | grep -e dummy -e obsolete -e transitional)
-   regarder les paquets nouvellement obsolete: aptitude search ?obsolete

