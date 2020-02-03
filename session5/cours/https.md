# Utiliser HTTPS avec son API REST

## HTTPS en quelques mots

[HTTPS](https://fr.wikipedia.org/wiki/HyperText_Transfer_Protocol_Secure) est le même protocole que HTTP mais avec une couche de **sécurité** en bonus. Concrètement, HTTPS permet de garantir :

- l'identité du site que l'on visite.
- la confidentialité des données échangées.
- l'intégrité des données échangées.

### L'identité du site

La vérification de **l'identité** du site est rendue possible grâce aux **certificats**. Le certificat est la **carte d'identité** d'un site. Un certificat peut-être généré **par les développeur•euse•s** (c'est ce que l'on fait généralement pour le développement ou les tests) ou généré par une **autorité de certification** (lorsque nos application sont en production).

> Evidemment, un certificat généré manuellement est comme un carte d'identité que l'on aurait faite nous même, il est valide pour _jouer_ avec son application en local mais n'a aucune valeur sur le web.

Les autorités de certification sont comme les **mairies** ou les **préfectures**, elle délivrent les certificats et **garantissent** votre identité. Il existe beaucoup d'autorités de certification, et beaucoup sont payantes comme [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.fr/fr/), [ComodoSSL](https://comodosslstore.com/). Mais depuis quelques années, nous pouvons compter sur [Let's Encrypt](https://letsencrypt.org/fr/) qui est gratuite !

Plusieurs types de certificats sont possibles. On a :

- Le **DV** pour _domain validation_.
- Le **OV** pour _organization validation_.
- Le **EV** pour _extended validation_.

Le **DV** est le plus simple à obtenir, il suffit de posséder un nom de domaine. Pour le **OV**, il faut en plus prouver que notre organisation existe. Enfin pour le **EV** il faut en plus prouver notre identité.

Pendant une période, on pouvait reconnaître les sites utilisant un certificat EV car on avait un petit cadenas vert dans la barre d'adresse avec le nom de l'entreprise. Mais plus aujourd'hui et pour diverses raisons que nous n'aborderons pas ici.

Lorsque notre navigateur reçoit un certificat, afin de prouver qu'il est valide, il utilise l'algorithme de [chiffrement asymétrique RSA](https://fr.wikipedia.org/wiki/Chiffrement_RSA).

Le certificat contient les **informations** du site en **clair** (domaine, organisation, ...). Ces informations sont **hashées** puis **signées** avec la **clé privée** du certificat (cette clé est évidemment gardée secrète par le serveur). Cette **signature** est ajoutée dans le certificat et peut être vérifiée grâce à la **clé publique** associée à la clé privée du certificat. Cette clé publique est **partagée en clair** dans le certificat et permet de **valider** la signature du certificat.

[Vidéo certificat HTTPS](../ressource/https/https.mp4)

### La confidentialité des données

Une fois l'identité du site vérifiée par notre navigateur, on peut commencer à échanger des données avec lui.

Et l'on souhaite que cet échange soit **chiffré** pour garantir la **confidentialité** de l'échange.

Pour ce faire, le navigateur va choisir une **clé de chiffrement symétrique** afin de chiffrer la communication. Le navigateur va **chiffrer** cette clé symétrique avec la **clé plublique RSA** contenue dans le certificat. Lorsque le serveur la reçoit il est le **seul** à pouvoir déchiffrer car il est le **seul** à avoir la **clé privée associée**. Il déchiffre donc la clé et la stocke.

La communication peut commencer.

### L'intégrité des données

**L'intégrité** des données quant à elle est **assurée** par un **simple hash** des données. Celui ci est **ajouté** au message et le destinataire **recalcule** ce hash pour vérifier que les données n'ont pas été altérées.

## La mise en pratique en développement pour une API Spring Boot

[Voir l'exercice HTTPS](../exercice/https.md)
