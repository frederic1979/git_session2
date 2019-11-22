# Les bases de données relationnelles

## Un peu de vocabulaire

Avant toute chose, il convient de définir ce qu'est une donnée. Une **donnée** est une **information relative à un objet**. On peut prendre l'exemple de la couleur d'une voiture. Il s'agit d'une donnée qui peut prendre la valeur _rouge_, _bleu_, _noir_, _jaune_, _vert_, _rose_ ... Dans ce cas là, on dira que la donnée est **qualitative**, car elle me permet de qualifier un objet. On peut aussi avoir des données **quantitatives**. Prenons l'exemple de la puissance du moteur de ma voiture. Cette donnée peut prendre une valeur entière numérique et strictement positive (entre 0 et ??? kW).

Une relation est un **lien** qui existe entre des choses. On peut reprendre l'exemple de la couleur d'une voiture, mais cette fois en spécifiant la couleur de _ma_ voiture. Dans ce cas on peut noter le lien entre un objet voiture et une personne.

Une **base de données relationnelle** est un système informatique qui permet de stocker des données tout en permettant de représenter les **liens** qui existent entre ces données. On pourrait par exemple stocker des _personnes_ et des _voitures_ et représenter les liens entre ces deux différentes choses (pour simplifier : une voiture peut appartenir à une seule personne, une personne peut avoir plusieurs voitures).

Les bases de données sont exploitables grâce à des logiciels : les **systèmes de gestion de base de données relationnelle**. Ils permettent de créer des bases de données, de stocker des données, de récupérer des données, ...

## Un peu d'histoire

Depuis la création des premiers systèmes informatiques, les **données** sont au coeur du réacteur. Les premières machines avaient très souvent un unique but et traitaient un type de données bien précis. Un exemple d'une toute première conçu pour exploiter des données de type texte est le [Colossus](https://cryptomuseum.com/crypto/colossus/index.htm) (un système conçu pour déchiffrer les messages que s'envoyaient les hauts dirigeants allemands pendant la seconde guerre mondiale).

Le premier ordinateur entièrement électronique est [l'ENIAC](https://fr.wikipedia.org/wiki/ENIAC). Il permettait de résoudre tous les problèmes calculatoire (additions, soustractions, multiplications et divisions avec des données numériques). On appelait d'ailleurs souvent les premières machines informatiques des **calculateurs**. Ces machines ont été inventées pour effectuer les calculs trop complexes à faire à la main. Dans le cas de l'ENIAC, il s'agissait de réaliser des calculs pour réaliser les tirs balistiques.

Le besoin de stocker les données et de les mettre en relation entre elles a très vite été rencontré. Les premières données stockées le furent de manière hierarchique. Cependant il pouvait être difficile de relier les données entre elles et d'autres problèmes (comme la redondance des données) pouvait rendre le traitement des données laborieux.

Dans les années 1970 l'anglais [Edgar Codd](https://history-computer.com/ModernComputer/Software/Codd.html) propose un système pour gérer les données sous forme de **tables** pouvant être liées entre elles. Chaque **table** doit représenter un **type d'objet** et dans les tables, les **colonnes** permettent de définir les **attributs** de l'objet et les lignes seront une instance d'un objet.

Si l'on prend à nouveau l'exemple des personnes et des voitures, on pourrait avoir deux tables, une table `Personne` ainsi qu'une table `Voiture`. La table `Personne` pourrait avoir les colonnes `identifiant`, `nom` et `prénom` et la table voiture avoir une colonne `identifiant`, `couleur`, `marque`, `modèle`, `puissance` et `id du propriétaire`. On pourrait avoir les lignes suivantes :

`Personne` :

| Identifiant | Nom      | Prénom     |
|-------------|----------|------------|
| 1           | Grand    | Jules      |
| 2           | Hugueney | Bernard    |

`Voiture` :

| Identifiant | Couleur  | Marque     | Modèle        | Puissance | Id du Propriétaire |
|-------------|----------|------------|---------------|-----------|--------------------|
| 1           | Jaune    | Renault    | Twingo        | 65        | 2                  |
| 2           | Rouge    | Ferrari    | Enzo          | 660       | 1                  |

Grâce à ce modèle, on peut stocker des données du même type dans une même table et faire des relations entre les tables grâce aux identifiants (plus de détails dans les sections à venir). On peut utiliser **l'algèbre relationnelle** pour effectuer des opérations sur les données comme des **sélections, des jointures, des unions, ...**.

## Le travail du•de la programmeur•euse

### Concevoir la base de données

Lors de la conception d'une base de données, on se base très souvent sur un **modèle de données**. On peut avoir défini un **diagramme de classe** objet en UML, on peut avoir créé un **modèle conceptuel de données**, ... Bref, on a des classes et des relations (ou des entités et des associations).

L'objectif est de passer de ce modèle à une base de données reprenant ce modèle dans un schéma (plan des relations entre tables).

Lors de la conception, on doit veiller à :

- garantir l'atomicité des données (un donnée atomique dans chaque colonne, par exemple pour un utilisateur on définit les colonnes : `nom`, `prénom` et `téléphone` et pas `nom complet` et `téléphone` car cela nous empècherait d'effectuer des opérations différentes sur les _noms_ et les _prénoms_).
- ne pas mélanger les données (une table pour chaque type de donnée : `Personne`, `Voiture`, ...)
- éviter la redondance des données (ne pas définir une même donnée dans deux tables différentes), sauf dans des cas bien précis d'amélioration des performances.

#### La création des tables

La première étape est de nommer la table. Il convient de choisir un nom permettant d'identifier le type d'objet que l'on souhaite stocker (`Personne`, `Voiture`, ...).

Vient ensuite la définition des colonnes.

##### Définir les colonnes

Lors de la définition de chaque colonne, il faut créer une colonne par attribut de l'objet que l'on souhaite stocker. Définir la colonne revient au minimun à donner le nom de l'attribut et à définir son type de donnée (par exemple pour le nom d'un personne on donnera le nom `nom` et on choisira le type de donnée `varchar`).

Une fois les colonnes créées, il convient de définir une clé primaire sur la table afin de pouvoir appliquer les opérations d'algèbre relationnelle.

##### Définition d'une clé primaire

Une **clé primaire** est un **identifiant unique** d'un enregistrement (ou ligne) d'une table. Cela peut-être n'importe quelle information permettant d'identifier une donnée. La base de données interdira ensuite toute insertion dans la table d'une donnée ayant la même clé. Pour une donnée de type `Personne` on pourrait imaginer utiliser le couple `nom` et `prénom` mais cela voudrait dire que des personnes ayant les mêmes _noms_ et _prénoms_ ne pourraient pas être stockées dans la même table. On pourrait alors penser à l'information _email_ qui doit en théorie être unique. Cependant en pratique on utilise très souvent un _identifiant_ qui est un nombre entier s'incrémentant automatiquement au fur et à mesure des insertions en table.

`Personne` :

| Identifiant | Nom      | Prénom     |
|-------------|----------|------------|
| 1           | Grand    | Jules      |
| 2           | Hugueney | Bernard    |

##### Définition de clés étrangères

Les **clés primaires** permettent d'identifier de manière unique un enregistrement. On peut donc les utiliser pour créer des **relations** entre différentes données. Lorsqu'on utilise la valeur d'une **clé primaire** identifiant un enregistrement dans une autre table, on parle de **clé étrangère**. Par exemple si j'ai une table `Personne` et une table `Voiture` et que je veux créer une relation entre les deux tables, je vais faire référence à la table `Personne` dans la table `Voiture` grâce à une clé étrangère dans la table `Voiture`.

`Voiture` :

| Identifiant | Couleur  | Marque     | Modèle        | Puissance | Id du Propriétaire |
|-------------|----------|------------|---------------|-----------|--------------------|
| 1           | Jaune    | Renault    | Twingo        | 65        | 2                  |
| 2           | Rouge    | Ferrari    | Enzo          | 660       | 1                  |

##### Définition de contraintes

On peut aussi appliquer des contraintes sur nos données afin d'assurer leur cohérence (on peut par exemple refuser des dates de naissances ulterieures à la date du jour, refuser les valeurs négatives pour une donnée de type puissance moteur).

### Exploiter la base de données

Une fois la conception effectuée, il est nécessaire de passer à la création de la base de données puis à son exploitation. Pour ce faire, on va utiliser un [système de gestion de base de données](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_base_de_donn%C3%A9es). Les logiciels de gestion de base de données permettent de dialoguer avec une base de données grâce au langage [SQL](https://fr.wikipedia.org/wiki/Structured_Query_Language). Ce langage permet à la fois d'éditer la structure des bases et de manipuler les données qu'elles contiennent.

Lorsque l'on écrit du code pour **éditer** la structure d'une base, on parle de [Data Definition Language](https://fr.wikipedia.org/wiki/Langage_de_d%C3%A9finition_de_donn%C3%A9es) et lorsque l'on en écrit pour **modifier** des données, on parle de [Data Modification Language](https://fr.wikipedia.org/wiki/Langage_de_manipulation_de_donn%C3%A9es).

Le langage SQL est **indépendant** des logiciels de gestion de base de données. La défition des tables et l'exploitation des données se fait donc de la même manière (ou presque) quel que soit le SGBD.

Quelques actions sont dépendantes du SGBD. La création d'une base (qui contiendra les tables) est par exemple dépendante du système. Nous verrons dans les exercices comment procéder.

#### Créer des tables de base de données

Voici comment créer la table `Personne` :

```sql
create table personne
(
  -- definition de la clé primaire
  id serial
    constraint personne_pk
      primary key,
  -- puis les autres colonnes
  nom varchar,
  prenom varchar
);
```

Et comment créer la table `Voiture` :

```sql
create table voiture
(
  -- definition de la clé primaire
  id serial
    constraint voiture_pk
      primary key,
  -- puis les autres colonnes
  couleur varchar,
  marque varchar,
  modele varchar,
  puissance int,
  -- puis la clé étrangère qui fait référence à la table personne
  id_proprietaire int
    constraint proprietaire_fk
      references personne
        on delete cascade
);
```

On peut aussi **supprimer des tables** (avec `drop table`), **modifier des tables** (avec `alter table`), **vider le contenu des tables** (avec `truncate table`) et bien plus encore !

#### Exploiter des données

Une fois nos tables créées on peut **insérer**, **mettre à jour** et **selectionner** des données.

##### Insérer des données

Voici comment insérer des données dans la table `Personne` :

```sql
insert into personne (id, nom, prenom) values (1, 'Grand', 'Jules');
insert into personne (id, nom, prenom) values (2, 'Hugueney', 'Bernard');
```

Voici comment insérer des données dans la table `Voiture` :

```sql
insert into voiture (id, couleur, marque, modele, puissance, id_proprietaire) VALUES (1, 'Jaune', 'Renault', 'Twingo', 65, 2);
insert into voiture (id, couleur, marque, modele, puissance, id_proprietaire) VALUES (2, 'Rouge', 'Ferrari', 'Enzo', 660, 1);
```

##### Mettre à jour des données

Imaginons que Bernard souhaite repeindre sa Twingo en bleu, il peut le faire facilement avec un `update` :

```sql
update voiture set couleur = 'Bleu' where id = 1;
```

Il est important de noter ici l'utilisation du mot clé `where`. Il permet de **restreindre** les lignes à modifier (dans ce cas on ne modifiera qu'une voiture, celle qui a l'ID #1). Si l'on oublie ce mot clé, les conséquences peuvent être **catastrophiques** (toutes les voitures de la table vont être modifiées et prendre la couleur _Bleu_).

##### Supprimer des données

Imaginons que je vende ma Ferrari, trop gourmande en essence. Je peux le faire facilement avec un `delete` :

```sql
delete from voiture where id = 2;
```

Il est important de noter ici aussi l'utilisation du mot clé `where`. Il permet de **restreindre** les lignes à supprimer (dans ce cas on ne supprimera qu'une voiture, celle qui a l'ID #2). Si l'on oublie ce mot clé, les conséquences peuvent être **catastrophiques** (toute les voitures de table vont être supprimées).

##### Selectionner des données

Une fois que l'on a des données dans les tables, on va avoir besoin de sélectionner nos données pour les visualiser. Grâce à l'algèbre relationnelle et au SQL on va pouvoir faire des opérations sur nos données.

###### Selection simple

Selection de toutes les personnes présentes dans la table et récupération de toutes les colonnes :

```sql
select * from personne;
```

Résultat :

| id          | nom      | prenom     |
|-------------|----------|------------|
| 1           | Grand    | Jules      |
| 2           | Hugueney | Bernard    |

Selection de toutes les personnes présentes dans la table et affichage des prénoms :

```sql
select prenom from personne;
```

Résultat :

| prenom     |
|------------|
| Jules      |
| Bernard    |

On peut aussi utiliser le mot clé `where` pour filtrer nos données :

```sql
select * from personne where prenom = 'Bernard';
```

Résultat :

| id          | nom      | prenom     |
|-------------|----------|------------|
| 2           | Hugueney | Bernard    |

###### Jointure

Le grand avantage des bases de données relationnelle est que l'on a des relations entre les tables. On peut utiliser les jointures pour aggréger les données :

```sql
select personne.nom, personne.prenom,
       voiture.marque, voiture.modele, voiture.couleur, voiture.puissance
from personne
join voiture on personne.id = voiture.id_proprietaire;
```

| nom      | prenom  | marque  | modele | couleur | puissance |
|----------|---------|---------|--------|---------|-----------|
| Hugueney | Bernard | Renault | Twingo | Jaune   | 65        |
| Grand    | Jules   | Ferrari | Enzo   | Rouge   | 660       |
