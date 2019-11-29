# Les bases du back en Java

## Pourquoi un serveur web en Java

**Mais d'abord, c'est quoi un serveur ?**

Le mot **serveur** peut avoir plusieurs sens.

On peut distinguer les serveurs **physiques** qui sont des **machines** tout le temps (ou presque) **allumées et connectées** au réseau (intranet ou internet). Comme pendant le projet météo, où nous nous sommes servi du Rapsberry Pi comme d'un serveur physique.

Les caractéristiques d'un serveur physique vont dépendre des besoins des applications que l'on va faire tourner dessus.

On peut avoir un tout petit serveur comme un Raspberry Pi pour mettre à disposition des mesures de température dans une salle de classe à destination d'un vingtaine de personnes. Comme on peut aussi avoir des serveurs très puissants pour répondre à une forte demande de ressources (nombre de connexions / puissance CPU / stockage / ...)

|              | Rasp       | Serveur Pro |
|--------------|------------|-------------|
| Mémoire vive | 1Go        | 256 Go      |
| Stockage     | 32Go       | 16 To       |
| CPU          | 4C 1.2GHz  | 16C 2.9GHz  |

Et on peut aussi parler de serveurs **logiciel**. En effet sur une machine qui reste tout le temps allumé, s'il n'y a aucun logiciel pour répondre au requêtes qui arrivent, il ne va pas se passer grand chose.

Si l'on reprend l'exemple de notre petit Raspberry Pi pour le projet météo, il y avait un serveur web applicatif Java qui permettaient de répondre à vos requêtes pour donner des informations sur les mesures (de température, pression et humidité) faites dans la salle.

**Pourquoi utiliser un serveur ?**

Dans le cadre d’un Système d’Informations (S.I.), on veut donner accès **simultané** à des informations à un nombre **indéterminé** d’utilisateurs et pouvoir répondre **à tout moment**.

On va donc mettre en place un serveur logiciel sur un serveur physique pour permettre l'accès à ces ressources (pages HTML, images, données, ...).

**Pourquoi utiliser un serveur web ?**

A partir d'ici nous emploierons le terme _serveur_ pour parler de serveur **logiciel**.

Un serveur web est en fait un serveur internet ou intranet, c’est-à-dire utilisant les protocoles de transport **TCP/IP** et utilisant le protocole de communication **HTTP**.

L’intérêt d’utiliser les protocoles **TCP/IP** est de tirer partie de toute l’infrastructure réseau existante.

**TCP/IP** permet de désigner une ressource à l’aide d’une URL. Cette URL indique :

- Le protocole (HTTP/HTTPS/FTP/...)
- Le nom du serveur (qui permet d’obtenir l’adresse IP grâce au DNS)
- Le port (par défaut 80 pour un serveur web en HTTP et 443 pour le HTTPS)

Pour le port, on devra tenir compte du fait que les ports _"de notoriété publique"_ (well known ports) comme le port 80, ne peuvent être utilisés par un simple utilisateur et requierent les privilèges administrateur. En pratique, on développera en utilisant un autre port disponible pour les simples utilisateurs et libre.

L’intérêt d’utiliser **HTTP** est de tirer parti de tous les logiciels/bibliothèques existantes, notamment les navigateurs web.

**Pourquoi utiliser un serveur web dynamique ?**

Les informations gérées par le S.I. peuvent être **modifiées** par les utilisateurs. En conséquence, il faut que le serveur puisse **générer dynamiquement** (en cours d’utilisation) les informations à envoyer. À contrario, un site web statique ne pourrait que servir des informations figées.

**Pourquoi utiliser un serveur web dynamique en Java ?**

Java est un langage populaire pour la réalisation de sites web dynamiques pour plusieurs raisons :

- Il est possible de gérer les connections de plusieurs utilisateurs en parallèle, tirant ainsi parti des architectures multi-cœurs des ordinateurs **[Concurrence / Parallelisme]**
- En plus de tirer parti de tous les cœurs d’un ordinateur, chacun de ceux-ci est utilisé efficacement grâce à la performance de la JVM **[Performance]**
- Grâce à la JVM, un serveur programmé en Java peut facilement être déployé sur n’importe quelle architecture disposant d’une JVM. Cela permet notamment d’externaliser l’hébergement du site (cf. cloud, IaaS voire PaaS) **[Portabilité]**
- Le fait que Java soit un langage compilé à typage statique aide à la réalisation de programmes fiables, même si les erreurs de compilation ne remplacent pas les tests ! **[Fiabilité]**
- Le fait que les autres qualités aient fait reconnaître l’intérêt d’utiliser Java pour la programmation de serveurs web a provoqué le développement de nombreuses bibliothèques et frameworks qui facilitent la programmation de serveurs. **[Rapidité de développement]**

## Changement de paradigme : inversion de contrôle & multithread

### Inversion de contrôle

Au niveau de l’architecture du code, il y a un changement fondamental entre les programmes _"classiques"_ en ligne de commande que nous avons implémentés jusqu’à présent et ceux que nous feront tourner sur serveurs.

Lorsque les programmes _"classiques"_ en ligne de commande sont lancés, ils effectuent une tâche en demandant éventuellement à l’environnement (utilisateur, disque, réseau, bases de données,…), des informations avant de produire un résultat et de se terminer.

Pour un **serveur**, comme pour certaines applications avec une interface graphique, **le programme n’a pas l’initiative : il passe son temps à attendre des requêtes/évènements pour y répondre.**

Le code qui implémente la réponse n’est pas appelé explicitement par le programme principal, mais enregistré pour être appelé lorsqu’une requête/un évènement survient.

### Multithread & accès concurrents

Pour des raisons de **qualité de service**, on voudra évidemment pouvoir répondre à plusieurs requêtes en même temps. On ne va pas attendre que notre voisin ait fini sa recherche Google pour lancer la notre, n'est-ce pas ?

On va donc répondre à ce besoin par l'utilisation du **multithread**.

Un **thread** est un fil d'éxecution. Un programme peut en contenir plusieurs et ils peuvent s'exécuter en **parallèle**.

On peut donc avoir un même bout de code s'exécutant en parallèle avec des paramètres possiblement différents. Dans le cas de l'API météo que nous avons utilisée si 5 personnes demandent en même temps la dernière mesure, notre serveur va faire 5 appels parallèle de la fonction de récupération de la dernière mesure pour répondre à tout le monde au même moment (ou presque).

C'est comme cela que notre code va gérer les multiples appels **simultanés**.

Il faudra garder cette notion en tête car cela peut poser un problème particulier si l’implémentation modifie un état partagé.
