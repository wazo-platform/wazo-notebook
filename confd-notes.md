
1.1
====

Varia
-----

 * Ajouter des "enabled" partout
   * Exposer les commented dans l'api rest 
 * Déplacer "voicemail_enabled" dans la ressource user-
   * ~~voicemail_enabled dans association user-voicemail -> user~~
 * ~~Mettre toutes les ressources au pluriel~~
   * ~~ex: /extensions/id/line  -> lines~~
 * ~~Migrer les anciens plugins au nouveau~~
   * ~~xivo_confd/resources dans xivo_confd/plugins~~
 * Séparer les notions de charger un API REST vs charger un service dans un plugin
   * ex: creer le service de device une seule fois dans le demon
 * ~~remplacer les anciens POST d'association par des PUT~~
   * ~~ex: POST /users/id/lines  -> PUT /users/id/lines/id~~
 * ~~Créer une ressource séparé pour les appels entrants~~
   * ~~but: associer les appels entrants vers autre chose qu'un user~~
 * ~~Retirer la notion d'association d'un appel entrant sur /lines/:id/extensions~~
   * ~~suite du point precedent~~


Suppression et déassociation
----------------------------

**Objectifs**:

 * réduire le nombre de requêtes nécessaire
 * simplifier la suppression

Déassocier automatiquement toutes les ressources associés

	DELETE /lines/:id?dissociate=1
	DELETE /lines/:id/dissociate

Supprimer automatiquement toutes les ressources associés

	DELETE /lines/:id?recursive=1
	DELETE /lines/:id/recursive

**remarques**

* deassociation a besoin d'un certain ordre
* /recursive plus facile pour controler les ACL

2.0
===

PUT vs PATCH
------------

 * PUT envoie la ressource au complet
 * PATCH envoie seulement les champs qui ont besoin d'être mis à jour

Liens
-----

**Objectif**: simplifier le modèle de données

Avant :

	{
		"id": 1,
		...
		"links": [
			{
				"rel": "users",
				"href": "http://confd:9486/1.1/users/1"
			}
		]
	}


Après

	{
		"id": 1,
		...
		"url": "http://confd:9486/1.1/users/1",
	}


Notes:
* peut servir lors de la pagination pour avoir directement l'url de la prochaine page, pas besoin de la calculer en js
* au lieu de mettre l'url complete, on peut mettre juste le path sans scheme/host/port

Slugs
-----

**Objectif:**

 * Réduire le nombre de requêtes
 * éviter de faire une recherche pour récupérer une ressource unique
 * rendre les URL plus parlants

Chaque ressource est récupérable de 2 façons :

 * ID
 * Représentation mnémotechnique (a.k.a un "slug")

Exemples:

	GET /users/:id
	GET /users/:lastname/:firstname
	GET /users/Sanderson/Lord

	GET /extensions/:id
	GET /extensions/:context/:exten
	GET /extensions/default/1000

Notes
* le tuple de slugs doit etre unique (pas lastname/firstname)

Erreurs
-------

Voir les specs dans [rest-api-errors.md](rest-api-errors.md).

Voir aussi: http://www.rfc-editor.org/rfc/rfc7807.txt


Suppression
-----------

**Objectif**:

 * réduire le nombre de requêtes
 * simplifier la suppression d'une ressource

Supprimer une ressource parent déassocie ou supprime automatiquement les ressources enfants, selon ce qui est le plus logique

Exemples:

	DELETE /users/:id
		#Supprime les touche de fonctions
		#Supprime la ligne
		#Déassocie la voicemail

	DELETE /lines/:id
		#Supprime l'endpoint
		#Supprime l'extension
		#Déassocie l'utilisateur


Créer, associer, déassocier
---------------------------

**Objectifs**

 * Réduire le nombre de requêtes
 * Simplifier la gestion d'associations
 * Réduire le overhead nécessaire côté client

Créer une nouvelle ligne et l'associer automatiquement à l'utilisateur

	POST /users/:id/lines

Associer une ligne qui existe déja

	PUT /users/:user_id/lines/:line_id

Déassocier une ligne qui existe déja

	DELETE /users/:user_id/lines/:line_id

Supprimer et déassocier toutes les lignes

	DELETE /users/:id/lines


Associations du parent
----------------------

**Objectifs**

 * Éviter des requêtes en trop pour récupérer de l'information
 * Réduire le overhead nécessaire côté client

Inclure des URLs dans la ressource parent qui pointe sur les ressources déja associés

Exemple:

	GET /users/:id

	{
		"id": 1,
		...
		"voicemail_url": "http://confd:9486/2.0/voicemails/2",
		"main_line_url": "http://confd:9486/2.0/lines/3",
		"secondary_line_urls": [
			"http://confd:9486/2.0/lines/4"
		]
	}


Collection d'associations
-------------------------

Les collections ne devrait pas utiliser le format de pagination (total, items). On ne peut pas filtrer ou paginer sur des collections d'associations

User-Line
---------

	GET /users/:id/lines/main
	GET /users/:id/lines/secondary
	GET /users/:id/lines

	{
		"main": {
			"id": 1,
			"context": "default",
			...
		},
		"secondary": [
			{
				"id": 1,
				"context": "default",
				...
			}
		]
	}

Line-User
---------

	GET /lines/:id/users

	{
		"main": {
			"id": 1,
			"firstname": "John",
			...
		},
		"secondary": [
			{
				id: 2,
				"firstname": "Sam",
				...
			}
		]
	}

Line-Extension
--------------

	GET /lines/:id/extensions
	{
		"extensions": [
			{
				"id": 34,
				"exten": "1000",
				"context": "default"
			}
		]
	}


User-Voicemail
--------------

	GET /users/:id/voicemails
	{

		"id": 10,
		"number": "1000"
		...

	}


Autres (idées)
--------------

 * Ne pas autoriser le post avec un champ non nullable (lors d'un put) à null


Multi-User (une ligne avec plusieurs users)
===========================================

 * supprimer code touche de fonctions (webi)
 * supprimer code provisionnement de poste (webi)
 * migrer la table usersip vers endpoint_sip
 * migrer les tables sccpline et sccpdevice vers endpoint_sccp
 * migrer la table usercustom vers endpoint_custom
 * migrer la table linefeatures vers line

Tables
------

###line

 * id
 * context
 * endpoint_id (NOT NULL)
 * device_id
 * device_position
 * registrar_id
 * provisioning_code
 * caller_id_name
 * caller_id_num
 * enabled

###endpoint

PK: (endpoint, endpoint_id)

 * endpoint (sip, sccp, custom) (NOT NULL)
 * endpoint_id (NOT_NULL)


###endpoint_sip

 * id
 * endpoint (default: sip)
 * type
 * host
 * options

###endpoint_sccp

 * id
 * endpoint (default: sccp)
 * options

###endpoint_custom

 * id
 * endpoint (default: custom)
 * interface
 * options

Multi-Line
==========

 * ~~séparer la table user_line en 2~~
   * ~~permet de gerer a la fois 1 user N lines ET 1 line N users~~
 * Créer une hiéarchie de caller_id

~~Tables~~
------

###~~user_line~~

~~PK: (user_id, line_id)~~

 * ~~user_id~~
 * ~~line_id~~
 * ~~main_user (boolean)~~
 * ~~main_line (boolean)~~

###~~line_extension~~

~~PK: (line_id, extension_id)~~

 * ~~line_id~~
 * ~~extension_id~~
 * ~~main_extension (boolean)~~

API
---

	POST /users/:id/lines #présentement utilisé pour associer
	PUT /users/:id/lines/:id
	GET /users/:id/lines
	GET-POST-PUT-DELETE /users/:id/lines/main
	GET-POST-PUT-DELETE /users/:id/lines/secondary

	GET /lines/:id/users
	GET-POST-PUT-DELETE /lines/:id/users/main
	GET-POST-PUT-DELETE /lines/:id/users/secondary
