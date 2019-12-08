# Une API REST, kezaco

## Mais pourquoi une API REST

Au début de l'histoire du web, nous avions seulement des pages HTML **statiques** stockées sur des serveur web statiques assurant leur envoi au client. Peu importe l'utilisateur•ice connecté•e la **réponse** à une requête sur une URL donnait **toujours** le même résultat.

Puis nous avons connu les premiers serveurs **dynamiques** permettant de générer les pages HTML de manière dynamique en fonction de paramètres envoyés par le client et des informations stockées dans les bases de données de chaque site. En fonction du client qui demandait la page et du moment où il demandait, le serveur pouvait renvoyer une page avec des informations et une structure différentes.

Puis avec la progression de l'utilisation de JavaScript les usages ont changé et les développeur•euse•s ont de plus en plus cherché à diminuer les rechargements de page afin de gagner en fluidité et confort d'utilisation. Ils•Elles faisait des appels au serveur pour récupérer des **données** et non plus des pages HTML complètes afin de ne recharger que quelques données dans les pages.

Aujourd'hui on l'observe très bien avec le concept de Single Page Application (SPA) où le HTML/CSS/JS est chargé une seule fois lorsque l'utilisateur•ice se connecte au site et ensuite le code JS va s'occuper de faire des appels HTTP au serveur pour charger les données dans le site.

Dans ce cas, plus besoin de générer les pages HTML côté serveur, il suffit simplement que notre serveur sache répondre aux requêtes **HTTP** pour créer/lire/modifier/supprimer des données. C'est ce que l'on va implémenter avec une API REST.

API signifie Application Programming Interface. Cela signifie que l'on va définir une interface que l'on peut utiliser par la programmation pour intéragir avec notre application.

[REST](https://fr.wikipedia.org/wiki/Representational_state_transfer) est un standard pour la définition de service web. Il impose un certain nombre de contraintes pour que toutes les API REST puissent être utilisées de la même façon.

En pratique on utilisera Spring boot qui est un framework qui permet de cadrer et simplifier le développement de ce type d'API en Java.

## Un peu plus de détails sur le protocole HTTP

Les API REST étant basées sur le protocole HTTP, il convient de détailler un peu plus ce protocole.

Le protocole HTTP est le protocole utilisé par les navigateurs pour communiquer avec les serveurs. Et pour ce faire, les navigateurs envoient des requêtes et les serveurs répondent ... des réponses.

Tous les détails ici : [Aperçu du protocole HTTP sur MDN](https://developer.mozilla.org/fr/docs/Web/HTTP/Aper%C3%A7u)

### Contenu d'une requête/réponse

#### 1. La méthode HTTP

##### GET

La méthode **GET** est celle qui est utilisée par un navigateur web lorsque l’on visite une page web en indiquant une URL ou en cliquant sur un lien. Cela correspond à la lecture des données associées à l’URL, sans modification des informations stockées côté serveur.

##### POST

La méthode **POST** est celle qui est utilisée par un navigateur web lorsque l’on envoie le contenu d’un formulaire. Cela correspond au cas général de l’envoi d’informations qui vont avoir un effet côté serveur.

##### PUT

La méthode **PUT** concerne elle l’envoi des données qui correspondent à l’URL, en réciproque de GET. Cette méthode doit être idempotente, c’est-à-dire qu’un même PUT doit pouvoir être répété plusieurs fois sans que le résultat soit différent côté serveur que si le PUT n’était fait qu’une seule fois.

##### DELETE

La méthode **DELETE** concerne elle la suppression des données qui sont à l’URL concernée.

#### 2. L'URL

La localisation des ressources auxquelles on souhaite accéder (page HTML, données, ...)

#### 3. Les entêtes

Aussi bien la requête que la réponse peuvent contenir des informations sous la forme **d'entêtes**. Il existe une longue liste d'entêtes **standard** et il est aussi possible d’en ajouter.

Un exemple standardisé : le **Content-Type**. Cet entête indique le type de contenu qui est renvoyé. Par exemple du HTML, qui est une sous-catégorie du texte, et l’encodage, par exemple l’utf-8: Content-Type: text/html; charset=utf-8.

#### 4. Le corps

La requête comme la réponse peuvent contenir un corps. Celui-ci contiendra les ressources à envoyer vers le serveur s'il s'agit d'une requête ou les ressources à envoyer au client s'il s'agit d'une réponse.

Dans le cas d'une requête, il peut s'agit de données à sauvegarder (dans le cas d'un POST par exemple).

Dans le cas d'une réponse, il peut s'agir de ressources demandées par la requête (données, page HTML, ...).

#### 5. Le status

Le code de statut accompagne la réponse du serveur pour informer sur la résultat de l'exécution de la requête.

Tout le monde connaît sans doute le fameux code 404 qui indique qu’il n’y a rien à l’URL indiquée, et il y a tout une [liste de codes](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) pour différents cas de figure.

- Les codes commençant par **2xx** indiquent que la requête a été **traitée avec succès**.
- Les codes commençant par **3xx** indiquent que la requête a été **redirigée**.
- Les codes commençant par **4xx** indiquent une **erreur venant du client**.
- Les codes commençant par **5xx** indiquent une **erreur venant du serveur**.

## Les règles du standard REST

Pour faire une API RESTful (qui respecte toutes les règles du standard) il faut s'accrocher. Nous aborderons ici les règles **élémentaires** qu'il convient de respecter.

On dit qu'une API REST expose des ressources. Les ressources sont à la fois les données et la logique de gestion de ces données.

On peut reprendre l'exemple de l'API météo. Notre API météo proposait les url suivantes :

- `http://192.168.1.197/last-measure`
- `http://192.168.1.197/top-measure/temperature`
- `http://192.168.1.197/top-measure/pressure`
- `http://192.168.1.197/top-measure/humidity`
- `http://192.168.1.197/measure/date?startDate=${startDateString}&endDate=${endDateString}`

C'était pratique et adapté dans le cadre de notre mini projet, mais ce n'est pas du tout standard.

Plusieurs problèmes existent dans cette API. Dans le cas de la météo, `last-measure` et `top-measure` sont juste des filtres particuliers sur une ressource **measure**. De plus, la dernière url retourne plusieurs **measures**, donc on devrait nommer cette ressource `measures`. Une meilleure proposition ci-dessous.

### Définir des chemins d'accès standard aux ressources

Pour notre API météo, nous aurions dû faire de la manière suivante :

- `http://192.168.1.197/measures?tob-by=date`
- `http://192.168.1.197/measures?top-by=temperature`
- `http://192.168.1.197/measures?top-by=pressure`
- `http://192.168.1.197/measures?top-by=humidity`
- `http://192.168.1.197/measures?startDate=${startDateString}&endDate=${endDateString}`

Imaginons maintenant une API où les ressources sont liées entre elles. On pourrait par exemple avoir une API gérant des villes et des monuments.

Il faut dans ce cas construire les url de cette façon :

- Pour récupérer toutes les villes : `http://ip-du-serveur/villes`
- Pour faire des actions sur la ville avec l'ID 1 : `http://ip-du-serveur/villes/1`
- Pour récupérer tous les monuments de la ville avec l'ID 1 : `http://ip-du-serveur/villes/1/monuments`
- Pour faire des actions sur le monuments avec l'ID 3 de la ville avec l'ID 1 : `http://ip-du-serveur/villes/1/monuments/3`

Et ainsi de suite si les monuments ont eux aussi des liens ...

Certain•e•s préfèrent parfois utiliser cette architecture pour récupérer des ressources liées : `http://ip-du-serveur/monuments?ville-id=1` afin d'avoir une architecture **flat**. Cela dépendra des choix de votre team. Ce qu'il faut c'est surtout **rester consistant dans vos choix !**

### Utiliser les méthodes HTTP comme opérations

De la même manière, il convient d'utiliser les méthodes HTTP pour des actions bien précises sur des ressources. Dans le cas du projet météo, nous n'utilisions que le **GET** et c'est normal car nous ne faisions que de la lecture de données.

Nous aurions pu imaginer mettre l'API sur un serveur partagé, et utiliser les petits Raspberry Pi comme des stations de mesure pour plusieurs salles et utiliser l'API avec **POST** pour enregistrer des mesures sur le serveur partagé.

Nous aurions pu aussi imaginer utiliser **PUT** pour modifier et **DELETE** pour supprimer une mesure si nécessaire.

Il faut retenir que chaque méthode a un rôle bien précis et qu'il convient de le respecter. Il est interdit de faire une requête du style `http://ip-du-serveur/villes/1/modify` pour modifier des données avec un **GET** ! C'est le rôle de **PUT**

Ce qu'il faut retenir c'est que l'on doit associer au CRUD, les méthodes HTTP :

- Create <=> POST
- Read <=> GET
- Update <=> PUT
- Delete <=> DELETE

### Utiliser les codes d'erreurs

Ne renvoyez par un code 200 si vous avez catché une exception par exemple, mais retournez un code d'erreur approprié (par exemple un code 400 si c'est à cause de données d'entrée invalides).

Et si vous ne respectez pas ces consignes, vous allez vous reconnaître dans [cette chanson](https://youtu.be/nSKp2StlS6s).