Installation/configuration LDAP
-------------------------------

-   Installer slapd

` # apt-get install slapd`

et mettre un mot de passe quelconque dont vous allez avoir de besoin lors pour la commande ldapadd...

-   Installer ldap-utils

` # apt-get install ldap-utils`

-   Noter votre basedn

` # slapcat | head -n1`
` dn: dc=lan-quebec,dc=avencall,dc=com`

Pour les prochains exemple, on supose que le basedn est "dc=lan-quebec,dc=avencall,dc=com". Remplacer cette valeur par la votre...

À partir de cette étape, vous pouvez soit installer phpldapadmin, soit ajouter manuellement les enregistrement avec ldapadd.

-   Installer phpldapadmin

` # apt-get install phpldapadmin`

` Ca va descendre apache2 si il n'y a pas de serveur web d'installer.`

-   Modifier le fichier /etc/phpldapadmin/config.php et remplacer toutes les occurences de 'dc=example,dc=com' par votre basedn.

-   Aller a <http://><ip>/phpldapadmin, logger vous avez l'utilisateur admin et ajouter des enregistrements.

ou

-   Créer un ldif avec un enregistrement "ou=people,<basedn>"

` # vi people.ldif`
` dn: ou=people,`<basedn>
` ou: people`
` objectclass: organizationalunit`

-   Ajouter l'enregistrement

` ldapadd -f people.ldif -xWD cn=admin,`<basedn>

-   Créer quelques utilisateurs pour vos tests...

` # vi users.ldif`
` dn: uid=alice,ou=people,`<basedn>
` objectclass: inetOrgPerson`
` cn: Alice`
` sn: alice`
` uid: alice`
` userpassword: foobar`
` telephoneNumber: 42301`
` mobile: 942301`
` mail: alice@example.org`
` `
` dn: uid=bob,ou=people,`<basedn>
` objectclass: inetOrgPerson`
` cn: Bob`
` sn: bob`
` uid: bob`
` userpassword: foobar`
` telephoneNumber: 42302`
` mobile: 942302`
` mail: bob@example.org`

-   Ajouter les enregistrements

` ldapadd -f users.ldif -xWD cn=admin,`<basedn>

Configuration SSL (ldaps) et StartTLS
-------------------------------------

### Première mise en place

#### Serveur Slapd

-   Créer un répertoire /etc/ldap/tls

`# mkdir /etc/ldap/tls`
`# cd /etc/ldap/tls`

-   Générer une clé privé et un CSR (les deux seront contenus dans le fichier serverkey.pem) :

`# openssl req -new -key serverkey.pem -out serverkey.pem`

-   Générer un certificat self-signed à partir de la clé privé et du CSR :

`# openssl x509 -req -days 3090 -in serverkey.pem -signkey serverkey.pem -out servercert.pem`

-   Valider le certificat :

`# openssl x509 -in servercert.pem -text -noout | less`
`# openssl verify servercert.pem`

-   Modifier /etc/default/slapd et s'assurer d'avoir une ligne du genre:

` SLAPD_SERVICES="`[`ldap:///`](ldap:///)` `[`ldaps://`](ldaps://)` ldapi:///"`

-   Modifier l'enregistrement cn=config

` dn: cn=config`
` add: olcTLSCertificateKeyFile`
` olcTLSCertificateKeyFile: /etc/ldap/tls/serverkey.pem`
` `
` dn: cn=config`
` add: olcTLSCertificateFile`
` olcTLSCertificateFile: /etc/ldap/tls/servercert.pem`

-   Redémarrer slapd

` # /etc/init.d/slapd restart`

#### Client LDAP (le XiVO)

-   Sur le xivo, ajouter le certificat (\*.crt) dans /usr/local/share/ca-certificates et exécuter update-ca-certificates

-   Editer le fichier /etc/ldap/ldap.conf et ajouter:

` TLS_CACERT /etc/ssl/certs/ca-certificates.crt`

-   Redemarrer spawn-fcgi

` # /etc/init.d/spawn-fcgi restart`

### Mise à jour du certificat (après expiration)

-   Utilise la clé et le csr existant (contenu dans le fichier serverkey.pem) et génère un nouveau certificat dans servercert.pem

`# openssl x509 -req -days 3090 -in serverkey.pem -signkey serverkey.pem -out servercert.pem`

-   Sur le xivo, ajouter le certificat dans /usr/local/share/ca-certificates et exécuter update-ca-certificates
