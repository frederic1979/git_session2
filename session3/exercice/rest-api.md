# Exercices API REST

## Etape 1 : Test d'une API existante

Pour se rendre compte de ce que nous allons devoir réaliser, on va d'abord tester une API existante : celle de [Star Wars](https://swapi.co/).

Installez l'application [Advanced Rest Client](https://install.advancedrestclient.com/install).

Essayez :

- De récupérer la liste des planètes
- De récupérer une seule planète
- De récupérer la liste des vaisseaux
- De récupérer un vaisseau

## Etape 2 : Setup d'un projet API

Nous allons réaliser la même API mais avec nos petites mains :-) (et Spring boot).

### Création d'un mini projet Spring boot

Choisir les dépendances suivantes :

- Spring Web
- Spring Data JPA
- PostgreSQL Driver

### Configuration du mini projet

Ouvrez le fichier `application.properties` et renseignez les propriétés suivante :

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/star_wars
spring.datasource.username=<votre username>
spring.datasource.password=<le mdp de votre username>
```

Cela permettra à Spring de se connecter à la base de données que nous avons créée pour Star Wars. Si vous souhaitez importer les données des planètes : [le schéma à utiliser](../ressource/correction/star-wars/star_wars.sql) et [les données](../ressource/correction/star-wars/insert.sql).

## Etape 3 : Création de l'API

### 1. Un cas d'utilisation simple : la liste de planètes

#### Création d'un controller Planet simpliste

Dans un premier temps :

- Créez un `PlantetController`
- Créez une fonction `listPlanets()` qui renvoie une liste vide
- Testez votre API avec **Advanced Rest Client**

#### Création de l'entité `Planet`

A l'aide de vos connaissances en JPA. Représentez sous forme d'une classe entité la ressource `Planet`.

#### Renvoyez quelques planètes

En les créant vous même dans le controller, renvoyez quelques planètes dans la fonction `listPlanets()` et testez votre API avec **Advanced Rest Client**. C'est magique, non ?

#### Renvoyez la vraie liste des planètes

Vous avez normalement, la liste des planètes dans votre base de données. Vous pouvez donc renvoyer la véritable liste des planètes. Et Spring nous donne un grand coup de main grâce aux **Repositories**.

Créez simplement une interface `PlanetRepository` qui étend l'interface `JpaRepository` et injectez votre repository dans le Controller. Vous avez magiquement accès à la fonction `findAll()`, génial, non ?

### 2. Le CRUD des planètes

Une fois échauffé avec la liste des planètes retournées, vous pouvez faire votre premier CRUD en REST dans le controller `PlanetController`.

Pour rappel, le CRUD, c'est :

- Create => POST d'une planète
- Read => GET d'une planète avec son ID
- Update => PUT d'une planète
- Delete => DELETE d'une planète avec son ID

### 3. On prend les même et on r'commence

Pour ceux qui avancent trop vite, vous faites la même chose pour les personnages, les espèces, les vaisseaux et les véhicules !
