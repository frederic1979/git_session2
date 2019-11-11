- [Types de clients](#org865966a)
  - [Clients SQL génériques](#org325b093)
  - [Clients spécifiques à une base de données](#org059d791)
- [Requêtes SQL](#org5251fc0)
  - [Sources de données](#orgeb1efc3)
  - [Expressions](#org89e222d)
  - [Tris : clause ORDER BY](#orged88017)
  - [Limitation du nombre de résultats : clause LIMIT et OFFSET](#org9fbaed9)
  - [Sélection de lignes : clause WHERE](#orgb9dc0f7)
- [Création de la table cities](#org18be0e2)
- [Destruction de table](#orgb1d0228)
- [Insertions dans la table cities](#org4ac2f09)
- [Suppression](#orgeab42bf)
- [Modification dans la table cities](#orgf81a44d)
- [Notion de transaction](#org5e3ed78)
- [Utilisation de SGBDR en Java : préliminaires](#org0cd79a4)
  - [Chargement de drivers](#org3463919)
  - [Établissement de la connection au SGBDR](#org82c832f)
- [Utilisation de SGBDR en Java : requêtes SQL](#org6f81d61)
  - [java.sql.Statement](#org8164828)
  - [java.sql.PreparedStatement](#org8907e01)
  - [Lecture des résultats d'une requête SELECT](#org38d87f2)
  - [Exemple de relation Many to Many, table d'associations](#org3d77a78)



<a id="org865966a"></a>

# Types de clients


<a id="org325b093"></a>

## Clients SQL génériques


<a id="org059d791"></a>

## Clients spécifiques à une base de données

<https://www.pgadmin.org/>

Il est ensuite possible de se connecter à `horton.elephantsql.com@5432` avec le login `vnzaekhx` et le mot de passe `oWN4ryvxxdjYWsko1u3WTW23k6yB7bM9` à la base de données du même nom que le login. Pour travailler, il est recommandé de :

-   créer votre propre base de données avec votre propre compte gratuit sur <https://www.elephantsql.com/>.
-   [installer postgresql](https://doc.ubuntu-fr.org/postgresql) sur son poste de travail.


<a id="org5251fc0"></a>

# Requêtes SQL

On peut effectuer des requêtes sur la base de données, soit à partir d'une console dédiée, soit à partir d'un programme. Les requêtes sont exprimées dans un langage spécifique, le **SQL**. Dans un premier temps, on effectuera les requêtes à partir de consoles dédiées, puis on verra comment effectuer des requêtes à partir d'un programme Java. Ensuite, on verra comment utiliser une base de données avec un programme Java sans avoir forcément besoin d'écrire des requêtes. En effet, la construction d'objets et même de collection d'objets, ou leur persistance peut être automatisée par un **ORM**. Finalement, on verra que l'on peut, à l'intérieur d'un programme Java, écrire des requêtes dans un autre langage, **JPQL**, qui permet d'avoir la flexibilité d'un langage tout en gardant les facilités introduites par un ORM.


<a id="orgeb1efc3"></a>

## Sources de données

Le langage SQL permet de sélectionner des données issues d'une source avec la clause `SELECT`. Avec la table `cities` comme source de données, on peut sélectionner toutes les données avec la requête SQL :

```sql
SELECT * from cities;
```

Le `*` indique que les données de toutes les colonnes doivent être retournées. On remarque, par rapport aux données stockées dans le fichier de la session précédente qui servent à initialiser les attributs des objets de la class `City`, qu'il y a en plus une colonne `id`. Celle-ci permet d'avoir une notion d'*identité* pour les enregistrements (lignes) d'une table (même que la référence sur un objet en Java) distincte de l'*égalité*. En base de données relationnelles, on parle de *clé primaire* d'un table pour désigner la colonne qui sert d'identifiant. On reviendra sur cette notion lors de la création de tables, en XXX.

On peut aussi ne spécifier que les colonnes qui nous intéressent, et indiquer l'ordre dans lesquelles les informations de chaque ligne doivent être retournées :

```sql
SELECT latitude, longitude, name
FROM cities;
```

Une base de données relationnelle peut bien évidemment, contenir plusieurs tables. Par exemple, la base contient une table `regions_name` avec les régions et le nom de leur capitale :

```sql
SELECT * from regions_name;
```

On peut sélectionner des données à partir de plusieurs tables, le résultat étant alors le produit cartésien (c'est-à-dire toutes les combinaisons possibles!) des différentes tables. L :

```sql
 SELECT * from regions_name, cities;
```

Cette requête retourne 643796 lignes! Bien sûr, en pratique, on utilisera le plus souvent pas toutes les lignes du produit cartésien entre deux table, mais on effectuera une *sélection* selon les valeurs de colonnes (et leurs relations). On verra notamment la notion de *jointure* à l'aide d'une *clé étrangère*.

De plus, celles-ci ne sont pas très lisibles car il y a deux colonnes `id` et deux colonnes `names`, une pour chacune des tables. Si l'on veut désigner une colonne, on peut (et on doit dans le cas de même nom dans plusieurs tables, comme pour `id` et `name`), préfixer le nom de colonne par le nom de la table :

```sql
 SELECT regions_name.name, regions_name.capital_name, cities.name, cities.longitude, cities.latitude from regions_name , cities;
```

Pour éviter de réécrire à chaque fois tout le nom de la table pour chaque préfixe, on peut à la place désigner un *alias* pour les sources de données :

```sql
 SELECT r.name, capital_name, c.name, c.longitude,c.latitude from regions_name as r, cities as c;
```

On peut aussi donner des noms aux colonnes du résultat avec le même mot-clé *as* :

```sql
SELECT regions_name.name as r_name, regions_name.capital_name as r_cname, cities.name, cities.longitude, cities.latitude from regions_name , cities;
```


<a id="org89e222d"></a>

## Expressions

En fait, chaque colonne de résultat peut être une expression en fonction de 0 ou plusieurs des colonnes de la ou des source(s) de données :

```sql
SELECT LOWER(name), UPPER(capital_name), CONCAT(name, ' / ',capital_name), 10 from regions_name;
```

Lorsque l'on utilise une ou des expressions ne faisant pas intervenir de colonnes de la ou des sources de données, on peut ne pas avoir de source de données du tout :

```sql
SELECT 10 as longitude_ref, 4 as latitude_ref;
```

Finalement, on pourra utiliser un résultat de sélection comme une source de données à la place d'une table, en donnant un alias à ce résultat :

```sql
SELECT cstes.long, cstes.lat FROM (SELECT 10 as long, 4 as lat) as cstes;
```

Il est donc possible de composer des requêtes SQL, par exemple pour retourner les noms de villes et leurs distances par rapport à une longitude/latitude de référence :

```sql
SELECT name
, (6371* acos(cos(radians(ref.latitude))) * cos(radians(cities.latitude)) * cos(radians(cities.longitude) - radians(ref.longitude))
+sin(radians(cities.latitude)) * sin(radians(cities.latitude))) AS distance
	FROM cities
    ,(SELECT 48.8 AS latitude, 2.4333 AS longitude) AS ref;
```

Afin de gagner en lisibilité, on peut composer les sélections sans pour autant les imbriquer, à l'aide de la formulation [WITH](https://www.postgresql.org/docs/current/static/queries-with.html) :

```sql
WITH ref AS (SELECT 48.8 AS latitude, 2.4333 AS longitude)
SELECT name
, (6371* acos(cos(radians(ref.latitude))) * cos(radians(cities.latitude)) * cos(radians(cities.longitude) - radians(ref.longitude))
+sin(radians(cities.latitude)) * sin(radians(cities.latitude))) AS distance
	FROM cities, ref;
```


<a id="orged88017"></a>

## Tris : clause ORDER BY

On peut trier les lignes de résultat en fonction d'une ou plusieurs expressions en fonction des valeurs des colonnes grâce à la clause [ORDER](https://www.postgresql.org/docs/current/static/queries-order.html) :

```sql
SELECT * from regions_name ORDER BY name ASC;
```

On peut classer par ordre croissant (`ASC`) ou décroissant (`DESC`). Si plusieurs critères de classement sont indiqués (séparés par des virgules) , ils sont appliqués de façon à ce qu'un critère serve à classer les lignes qui sont équivalentes selon les crières précédents.


<a id="org9fbaed9"></a>

## Limitation du nombre de résultats : clause LIMIT et OFFSET

Il est possible de ne récupérer qu'une partie des résultats d'une requête grâce aux clauses [LIMIT et OFFSET](https://www.postgresql.org/docs/current/static/queries-limit.html). `LIMIT` permet de ne récpérer qu'un nombre limité de résultats. Par exemple pour ne récupérer que 10 lignes :

```sql
SELECT * from cities LIMIT 10;
```

La clause `OFFSET` permet, elle, de ne considérer les résultats qu'après avoir passé un nombre de lignes données. Les deux clauses peuvent être combinées pour implémenter une pagination. Par exemple, on peut récupérer 10 résultats après avoir passé les 10 premiers :

```sql
SELECT * from cities LIMIT 10 OFFSET 10;
```

Bien sûr, ces clauses sont le plus utiles lorsqu'elles sont combinées avec une clause de classement :

```sql
SELECT * from cities ORDER BY name ASC LIMIT 10 OFFSET 10;
```

Voire :

```sql
WITH ref AS (SELECT 48.8 AS latitude, 2.4333 AS longitude)
SELECT name
, (6371* acos(sin(radians(ref.latitude)) * sin(radians(cities.latitude)) + cos(radians(cities.latitude)) * cos(radians(ref.latitude)) *
 cos( radians(ref.longitude) - radians(cities.longitude)))
+sin(radians(cities.latitude)) * sin(radians(cities.latitude))) AS distance
	FROM cities, ref ORDER BY distance ASC LIMIT 10;
```

En traduisant en SQL la fonction de distance entre coordonnées GPS basée sur la [loi des cosinus en coordonnées sphériques](https://fr.wikipedia.org/wiki/Loi_des_cosinus#En_g.C3.A9om.C3.A9trie_sph.C3.A9rique) . Avec une formule plus précise de [Distance du grand cercle](https://fr.wikipedia.org/wiki/Distance_du_grand_cercle), on a :

```sql
WITH ref AS (SELECT 48.8 AS latitude, 2.4333 AS longitude),
delta_radians AS (SELECT name, latitude, longitude, radians(cities.latitude - ref.latitude) as delta_latitude, radians(cities.longitude - ref.longitude) as delta_longitude FROM cities, ref),
sin_dr AS ( SELECT name, latitude, longitude, sin(dr.delta_latitude/2) as lat, sin(dr.delta_longitude/2) as long FROM delta_radians as dr),
tmp AS (SELECT name, sin_dr.lat * sin_dr.lat + cos(radians(sin_dr.latitude)) * cos(radians(ref.latitude)) * sin_dr.long * sin_dr.long as a FROM sin_dr, ref)
SELECT name
, (6371 * 2 * atan2(sqrt(a), sqrt(1-a))) as distance
	FROM tmp ORDER BY distance ASC LIMIT 10;
```


<a id="orgb9dc0f7"></a>

## Sélection de lignes : clause WHERE


<a id="org18be0e2"></a>

# Création de la table cities

En fait, on va créer la table `cities` sur le serveur Postgresql distant à partir d'une sélection des colonnes d'une table d'une base de données existante. La table source sera sur le serveur MySQL distant hébergé gratuitement à `jdbc:mysql://db4free.net:3306/random_user` avec les login est mot de passe : `random_user` et `1mot2passe`, à partir des donnés mises à disposition par [données mises à disposition par Tony Archambeau](http://sql.sh/736-base-donnees-villes-francaises).

La table destination sera sur le serveur Postgresql distant vu plus haut XXX.

On va créer la table city sur le serveur postgresql avec la commande SQL suivante :

```sql
      CREATE TABLE cities (
      id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      departement VARCHAR(3),
      postal_codes VARCHAR(255),
      pop_1999 INTEGER CHECK (pop_1999 >= 0),
      pop_2010 INTEGER CHECK (pop_2010 >= 0),
      pop_2012 INTEGER CHECK (pop_2012 >= 0),
      area DOUBLE PRECISION  CHECK (area >= 0.),
      longitude DOUBLE PRECISION NOT NULL,
      latitude DOUBLE PRECISION NOT NULL,
      z_min INTEGER,
      z_max INTEGER,
      CHECK (z_min <= z_max));
```

-   La colonne `id` est une clé primaire (*PRIMARY KEY*) qui permet donc l'identification de chaque ligne de la table. On laissera la base de données attribuer une valeur unique à chaque nouvelle ligne ajoutée à la table (on mettra `DEFAULT` en valeur). On indique à la base d'utiliser des valeurs entières successives (`SERIAL`). La base de donnée s'assure que les valeurs des identifiants sont uniques dans la table : deux lignes ne peuvent pas avoir la même valeur de clé primaire. De plus, comme la recherche d'une ligne à partir de la valeur de son identifiant doit être très rapide, la clé primaire est automatiquement associée à un *index* qui permet d'accélérer les recherches.

-   La colonne `name` contiendra une chaîne d'au maximum 255 caractères et n'autorise pas de valeur manquante (`NULL`).

-   La colonne `departement` contiendra une chaîne d'au maximum 3 caractères pour le code du département de la ville.

-   la colonne `postal_codes` contiendra une chaîne d'au maximum 255 caractères pour stocker le ou les codes postaux de la ville. En cas de plusieurs codes postaux, ceux-ci sont séparés par le caractère '-'. Ce n'est pas la représentation la plus pratique d'une liste, et nous verrons en XXX d'autres solutions.

-   les colonnes `pop_1999`, `pop_2010` et `pop_2012` contiennent les populations (si elles sont connues) en 1999, 2010 et 2012 sous la forme de nombres entiers. Là encore, cette représentation (une colonne par année) a des inconvénients, notamment l'impossibilité d'ajouter de nouvelles données lorsqu'elles seront disponibles. On réfléchira à d'autres solutions en XXX.

-   la colonne `area` contient la surface de la ville en km² sous la forme d'un nombre à virgule flottante en double précision.

-   les colonnes `longitude` et `latitude` contiennent les longitude et latitude en degrés sous la forme de nombres à virgule flottante double précision. Cette colonne interdit les valeurs manquantes (`NULL`).

-   les colonnes `z_min` et `z_max` contiennent, lorsqu'elles sont disponibles, les altitudes minimales et maximales de la ville, sous la forme de nombres entiers de mètres.

Si une table avec le nom utilisé dans la commande `CREATE TABLE` existe déjà, la création échoue.

On remarque la correspondance de l'*ORM* (Object-Relational Mapping) entre classes et tables et entre colonnes et attributs (et donc entre lignes et objets). On note les différences suivantes :

-   la notion de *clé primaire* qui est nécessaire, en plus des colonnes pour les attributs, afin de gérer l'identité des enregistrements.
-   le fait qu'en plus d'avoir des types, les colonnes peuvent avoir des contraintes, notamment :
    -   sur chaque valeur, par exemple le fait de pouvoir être une valeur manquante ou non, ou sur le domaine de validité (par exemple le fait d'être une valeur positive).
    -   sur l'ensemble des valeurs d'une colonne, par exemple la contrainte d'unicité (implicite pour les clés primaires).
    -   sur plusieurs colonnes, par exemple le fait qu'une valeur doive être inférieure ou supérieure à une autre. Il est possible, et même recommandé, de [nommer les contraintes](https://en.wikipedia.org/wiki/Check_constraint), afin d'avoir des messages d'erreur plus explicites. Attention ! [Certaines bases de données ignorent les contraintes de type CHECK](https://dev.mysql.com/doc/refman/5.7/en/create-table.html) !
-   le fait que les chaînes de caractères sont le plus souvent implémentées avec une taille maximale prédéterminée (pour des raisons de performance). En fait, certains systèmes de gestion de bases de données proposent un type `text` pour stocker des chaînes de caractères sans limite de taille à priori, mais ce n'est pas un type du standard SQL.

Au niveau des chaînes de caractères, contrairement à Java, il y a [plusieurs possibilités d'encodage](https://www.postgresql.org/docs/current/static/multibyte.html). On s'assurera en général d'utiliser le plus standard : UTF-8.

À titre d'exercice, on peut créer d'autres tables, par exemple avec des contraintes nommées.


<a id="orgb1d0228"></a>

# Destruction de table

On peut détruire une table avec l'instruction `DROP TABLE` :

```sql
CREATE TABLE to_drop(id SERIAL PRIMARY KEY);
DROP TABLE to_drop;
```

**Attention !** Il y'a pas de possibilité de revenir en arrière sur l'effacement d'une table. Bien s'assurer qu'on efface bien la table voulue (et qu'on est bien sur le serveur de base de données voulu, pas sur le serveur de production plutôt que sur celui de développement ou de test !).


<a id="org4ac2f09"></a>

# Insertions dans la table cities

On va ajouter une ville dans la base, par exemple le village disparu [Ailles](https://fr.wikipedia.org/wiki/Ailles) avec les informations suivantes :

-   **nom:** Ailles
-   **département:** 02
-   **populations:** 0 pour toutes les années considérées
-   **superficie:** 4.69 km²
-   **longitude:** 4.1528
-   **latitude:** 49.3493

```sql
INSERT INTO cities VALUES(DEFAULT, 'Ailles', '02', NULL, 0,0,0, 4.69, 4.1528, 49.3493, NULL, NULL);
```

On peut vérifier qu'une tentative d'insertion de valeurs ne respectant pas les contraintes est rejetée (sous réserve que l'on utilise pas [un SGDBR qui ignore certaines contraintes](https://dev.mysql.com/doc/refman/5.7/en/create-table.html) :

```sql
INSERT INTO cities VALUES(DEFAULT, 'longitude invalide', '02', NULL, 0,0,0, 4.69, NULL, 49.3493, NULL, NULL);
```

À titre d'exercice, on peut vérifier l'erreur provoquée par la tentative d'insertion d'une ligne dont le département est invalide, soit pour une erreur de type, soit parce que la chaîne de caractères serait trop longue.

```sql
INSERT INTO cities VALUES(DEFAULT, 'pop invalide', '02', NULL, -1,0,0, 4.69, 4.1528, 49.3493, NULL, NULL);
```

et

```sql
INSERT INTO cities VALUES(DEFAULT, 'z invalides', '02', NULL, 0,0,0, 4.69, 4.1528, 49.3493, 1, -1);
```

Pour ces dernières contraintes, le message d'erreur sera plus ou moins explicite selon qu'on aura ou non nommé la contrainte violée.

On va aussi ajouter des villes imaginaires afin de pouvoir faire des modifications sans invalider des données réelles :

```sql
INSERT INTO cities VALUES(DEFAULT, 'Ville d''en haut', NULL, NULL, 100, NULL, NULL, 4.69, 5.0, 50.0, NULL, NULL);
INSERT INTO cities VALUES(DEFAULT, 'Ville d''en bas', NULL, NULL, 100, NULL, NULL, 4.69, 5.0, 50.0, NULL, NULL);
```


<a id="orgeab42bf"></a>

# Suppression

On peut supprimer la première ville que l'on a ajoutée de la façon suivante :

```sql
DELETE FROM cities WHERE name='Ailles';
```

Attention, si la clause `WHERE` sélectionne plusieurs lignes, elles seront toutes effacées. **Attention !** En l'abscence de clause `WHERE`, **TOUTES LES LIGNES SERONT EFFACÉES !**

En pratique, il est souvent plus prudent de faire un `SELECT` avec la clause `WHERE` pour s'assurer que l'on ne sélectionne pas plus de lignes que prévu. Ensuite, on remplace le `SELECT` par un `DELETE` sans toucher à la clause `WHERE` pour être sûr que ce sont bien les mêmes lignes qui seront effacées.


<a id="orgf81a44d"></a>

# Modification dans la table cities

Supposons que l'on veuille modifier les valeurs d'un ou plusieurs attributs, par exemple pour modifier la valeur de la population en 2010 d'une ville que l'on a ajoutée :

```sql
UPDATE cities SET pop_2010= 1000 WHERE name='Ville d''en haut';
```

On peut bien sûr utiliser n'importe quelle expression pour la nouvelle valeur, en utilisant éventuellement les valeurs de la ligne modifiée :

```sql
UPDATE cities SET pop_2010= pop_2010 + 0.5 * pop_1999 WHERE name='Ville d''en haut';
```

On peut aussi modifier plusieurs lignes à la fois lorsque la clause `WHERE` en sélectionne plus d'une :

```sql
UPDATE cities SET pop_2012= 2 * pop_1999 +1 WHERE name LIKE 'Ville d''en %';
```

**Attention !** En l'absence de clause `WHERE`, ce sont **toutes les lignes** de la table qui seront modifiées !


<a id="org5e3ed78"></a>

# Notion de transaction

On peut vouloir faire plusieurs modifications "en même temps", ou plus exactement de façon atomique. C'est-à-dire que l'ensemble des modifications soit effectué ou alors qu'aucune modification ne soit effectuée. On peut utiliser pour cela une *transaction*. On commence explicitement une transaction avec l'instruction SQL `START TRANSACTION` et ensuite, si tout c'est bien passé en enregistre les résultats de la transaction avec l'instruction SQL `COMMIT`. En cas d'erreur, on peut annuler tout ce qui a été fait depuis le début de la transaction avec l'instruction `ROLLBACK`.

Attention ! La plupart des consoles permettant d'envoyer des commandes SQL à un SGBDR sont en mode 'auto-commit' où chaque instruction est considérée comme étant dans une transaction terminée par un commit. Pour tester les effets d'une transaction explicite, il est nécessaire de désactiver l'auto-commit.

Par exemple, si l'on veut déplacer 75 personnes de la population de 'Ville d'en haut' en 1999 vers la population de 'Ville d'en bas' la même année :

```sql
SELECT * from cities WHERE name LIKE '%Ville d''en %';
START TRANSACTION;
UPDATE cities SET pop_1999= pop_1999 + 75 WHERE name = 'Ville d''en bas';
UPDATE cities SET pop_1999= pop_1999 - 75 WHERE name = 'Ville d''en haut';
COMMIT;
SELECT * from cities WHERE name LIKE '%Ville d''en %';
```

Mais si l'on essaie répéter ces opérations une deuxième fois (pourvu que la population de 'Ville d'en haut' soit trop faible et que les contraintes d'intégrité soient honorées), la deuxième instruction sera rejetée :

```sql
SELECT * from cities WHERE name LIKE '%Ville d''en %';
START TRANSACTION;
UPDATE cities SET pop_1999= pop_1999 + 75 WHERE name = 'Ville d''en bas';
SELECT * from cities WHERE name LIKE '%Ville d''en %';
UPDATE cities SET pop_1999= pop_1999 - 75 WHERE name = 'Ville d''en haut';
```

On peut vérifier que la première a bien eu un effet avec une instruction `SELECT`, mais on peut revenir en arrière sur cette modification à l'aide d'un `ROLLBACK` :

```sql
SELECT * from cities WHERE name LIKE '%Ville d''en %';
ROLLBACK;
SELECT * from cities WHERE name LIKE '%Ville d''en %';
```

Attention ! On pourrait être tenté de vouloir vérifier à l'avance si un ensemble de modifications sera possible sans violations de contraintes. C'est cependant impossible dans le contexte d'un **serveur** de bases de données. En effet, entre l'instant où l'on vérifie une condition et celui où on effectue une modification en fonction de cette condition, les données de la base peut avoir été modifiées ! La seule façon de savoir si une modification peut être faite sans violation de contrainte, c'est d'essayer de faire la modification et de constater si elle a pu être effectuée ou non. D'où la nécessité d'utiliser des transactions si plusieurs modifications doivent être toutes effectuées ensemble ou aucune ne doit être effectuée si l'une d'elles échoue.


<a id="org0cd79a4"></a>

# Utilisation de SGBDR en Java : préliminaires

Les SGDBR et leurs drivers Java permettent différents niveaux de fonctionnalités. Dans un soucis de simplicité et de compatibilité maximale, on ne s'intéresse ici qu'aux fonctionnalités les plus basiques dont la disponibilité est garantie. En cas de besoin, et si le SGDBR est connu et fixé, on pourra utiliser [des fonctionnalités plus avancées](https://docs.oracle.com/javase/tutorial/jdbc/basics/retrieving.html).


<a id="org3463919"></a>

## Chargement de drivers

Tout d'abord, il faut utiliser le(s) driver(s) JDBC (Java DataBase Connectivity) adapté(s) au(x) SGBDR utilisé(s).

Ensuite, il faut rendre les drivers accessibles au programme Java. Habituellement, il suffit d'utiliser `import` pour utiliser n'importe quelle classe (sous réserve qu'elle soit disponible dans le `CLASSPATH` lors de la compilation et de l'exécution du programme.

Dans le cas des classes de drivers JDBC, on veut pouvoir choisir le SGDBR, et donc le driver, à l'exécution et non à la compilation. En effet, on peut vouloir utiliser différents SGDBR en environnement de test et en production. Évidemment, il faut que ce soit le même programme compilé qui soit exécuté en test et en production. Pour la même raison, parce que les URL d'accès au SGBDR et les comptes (login et mot de passe associé) ne sont pas forcément les mêmes en test et en production, on fera aussi en sorte que ces informations soient aussi paramétrables sans recompilation, donc hors du code source.

En fait, pour les mots de passe, il est aussi essentiel de ne jamais les écrire dans un code source. En effet, les codes sources sont souvent diffusés largement, notamment par des systèmes de gestion de version et doivent donc contenir aucune information confidentielle. Par exemple, lorsqu'on stocke des informations confidentielles dans un fichier .properties dans un projet géré par git, il est essentiel d'exclure ce fichier de la gestion de version à l'aide de [gitignore](https://git-scm.com/docs/gitignore).

Pour que les classes des drivers JDBC soient chargées dynamiquement (à l'exécution), il faut exécuter la méthode statique `forName` de la classe [Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html) :

-   pour Postgresql :

```java
Class.forName("org.postgresql.Driver");
```

-   pour H2 :

```java
Class.forName("org.h2.Driver");
```

-   pour MySQL :

```java
Class.forName("com.mysql.jdbc.Driver");
```

Cet appel de méthode peut lancer une exception de type `ClassNotFoundException` qu'il faut donc gérer.

Ensuite, le driver correspondant au SGBDR sera choisi en fonction de l'URL de connection à la base. Cette URL étant dans une chaîne de caractères, elle est donc aussi configurable à l'exécution.


<a id="org82c832f"></a>

## Établissement de la connection au SGBDR

La connection au SGDBR est matérialisée par un objet instance d'une classe implémentant l'interface [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html) . Cette connection peut être en [mode autocommit ou non](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#getAutoCommit()). On récupère cet objet par un appel à la méthode [java.sql.DriverManager.getConnection()](https://docs.oracle.com/javase/7/docs/api/java/sql/DriverManager.html#getConnection(java.lang.String,%20java.lang.String,%20java.lang.String)). Par exemple, si les URL, login et mot de passe sont stockés dans une `Map<String,String> env` et assocés aux clés `"URL"`, `"USER"` et `"PASS"` :

```java
Connection conn= DriverManager.getConnection(env.get("URL"), env.get("USER"), env.get("PASS"));
```

L'url étant de la forme "jdbc:SGBD\_NAME://DBSERVER\_NAME:DBSERVER\_PORT/DATABASE\_NAME".

Il faudra s'assurer que la connection sera fermée à un appel à la méthode [close()](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#close()). On remarque que l'interface `java.sql.Connection` hérite de l'interface `java.lang.AutoClosable`, ce qui implique donc qu'on peut faire l'initialisation dans un bloc `try(){}` (dit «try with resources»). Attention : cette méthode `.close()` peut elle-même lancer une [SQLException](https://docs.oracle.com/javase/7/docs/api/java/sql/SQLException.html) qu'il faut donc aussi gérer.

On passera l'objet connection aux différentes méthodes qui s'en serviront pour interagir avec le SGBDR.


<a id="org6f81d61"></a>

# Utilisation de SGBDR en Java : requêtes SQL

Il y a deux façons de faire exécuter des requêtes SQL en Java, suivant qu'on utilise des [java.sql.Statement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html) ou des [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html).


<a id="org8164828"></a>

## java.sql.Statement

On commence par créer l'objet par un appel à [createStatement()](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#createStatement()) sur l'objet qui implémente l'interface `Connection`. Cet objet nouvellement créé devra lui aussi être fermé par un appel à sa méthode [close()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#close()). Comme il implémente l'interface `AutoCloseable`, on peut créer l'objet dans un `try(){}` («try with resources»).

Ensuite, on peut appeler sur cet objet l'une des méthodes suivante :

-   [execute(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#execute(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour un booléen indiquant si l'exécution s'est déroulée sans erreur ou non.
-   [executeUpdate(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeUpdate(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour le nombre de lignes modifiées (comme son nom l'indique, on utilise cette méthode pour des commandes SQL `UPDATE`).
-   [executeQuery(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeQuery(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour un objet implémentant l'interface [java.sql.ResultSet](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html) qui permettra de récupérer les résultat d'une commande SQL `SELECT`.

De plus, si l'on veut exécuter plusieurs commandes SQL en une seule fois, pour des raisons de performance, on peut à la place utiliser la méthode [addBatch(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#addBatch(java.lang.String)) pour chacune des commandes, puis déclencher l'exécution de toutes celles-ci par un appel à [executeBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeBatch()).

Souvent, la commande SQL à exécuter dépend de valeurs qui ne sont connues qu'à l'exécution, par exemple les données à ajouter dans un `INSERT` ou des critères d'une clause `WHERE`. Il est possible de construire dynamiquement la commande SQL en concaténant des chaînes de caractères mais il faut alors faire très attention au risque d'[injection SQL](https://fr.wikipedia.org/wiki/Injection_SQL). Même sans utilisateurs hostiles, il faut de toutes façons prendre en compte l'échappement des caractères spéciaux dans une chaîne de caractères. Par exemple, le guillemet simple, utilisé souvernt pour l'apostrophe, doit être remplacé par deux guillemets simples pour éviter qu'il soit interprété comme la fin de chaîne. On peut faire pour cela un appel comme ceci : `.replaceAll("'","''")`.

Il est cependant préférable d'utiliser des [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html) pour ne pas avoir à gérer soi-même les arguments.


<a id="org8907e01"></a>

## java.sql.PreparedStatement

Toujours à partir de l'objet implémentant l'interface [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html), on peut utiliser la méthode [prepareStatement(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#prepareStatement(java.lang.String)) pour créer un objet implémentant l'interface [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html). La chaîne de caractère passée en argument contient le code de la commande SQL avec des '?' à la place des arguments de la commande. Par exemple, pour insérer une nouvelle ligne dans notre table `cities`, on pourra utiliser :

```java
String insertCmd= "INSERT INTO cities VALUES(DEFAULT, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);";
try(PreparedStatement stmt= conn.prepareStatement(insertCmd)){
}
```

Comme pour la création d'un [java.sql.Statement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html), on peut (devrait ?) utiliser un *try with resources* parce que l'objet créé implémente l'interface `java.lang.AutoCloseable`.

Ensuite, on peut utiliser sur cet objet les méthodes `setXXX()` comme [setDouble(int parameterIndex, double parameterValue)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setDouble(int,%20double)) ou [setString(int parameterIndex, String parameterValue)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setString(int,%20java.lang.String)) pour donner des valeurs à chacun des paramètres représentés par un '?' dans la chaîne passée en argument de [prepareStatement(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#prepareStatement(java.lang.String)). Attention ! Les `parameterIndex` commencent à 1 et non à 0. Si l'on veut insérer une valeur manquante `NULL`, il faut utiliser la méthode [setNull(int parameterIndex, int sqlType)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setNull(int,%20int)). L'argument `sqlType` étant l'une des constantes nommées définies dans la classe [java.sql.Types](https://docs.oracle.com/javase/7/docs/api/java/sql/Types.html).

Ensuite, une fois que tous les arguments on reçu une valeur, on peut appeler l'une des méthodes [execute()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#execute()), [executeQuery()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeQuery()) ou [executeUpdate()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeUpdate()). On peut aussi créer un batch de plusieurs commandes à executer à l'aide des méthodes [addBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#addBatch()) et [executeBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeBatch()).


<a id="org38d87f2"></a>

## Lecture des résultats d'une requête SELECT

Lorsque l'on exécute une requête `SELECT`, on utilise la méthode [executeQuery()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeQuery()) qui retourne un objet implémentant l'interface [java.sql.ResultSet](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html). Cet objet permet de récupérer chacunes des données de chacune des lignes correspondant à la requête. Pour passer à la ligne suivante en testant s'il y en a une, on utilise la méthode [next()](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#next()) (le plus souvent comme condition de continuation dans une boucle `while()` pour traiter toutes les lignes de la première à la dernière). Ensuite, pour chacune des lignes (à l'intérieur de la boucle, donc), on peut récupérer la valeur de chacune des colonnes avec des appels aux méthodes [getDouble(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getDouble(java.lang.String)), [getInt(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getInt(java.lang.String)), [getLong(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getLong(java.lang.String)), [getString(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getString(java.lang.String)) et autres. Il est aussi possible de passer des numéros de colonne en argument plutôt que d'utiliser les noms, mais il faut alors se souvenir non seulement de l'ordre des colonnes dans le resultat, mais aussi que leur numérotation commence à 1 et non à 0. Toujours dans un soucis de plus grande compatibilité avec tous les drivers JDBC disponibles, mais aussi dans un soucis de performance, il est préférable de se contenter de lire les lignes les unes après les autres et pour chaque ligne et de ne lire les données qu'une seule fois pour une instance de `ResultSet` donnée.

Par exemple, pour construire une liste d'objets de classe `CityDTO` à partir du résultat d'une requête SQL sur une connection donnée, on pourrait écrire :

```java
        private static List<CityDTO> readValues(Connection conn){
            List<CityDTO> res= new ArrayList<CityDTO>();
            try(Statement stmt= conn.createStatement()){
                ResultSet rs= stmt.executeQuery(readQuery);
                while(rs.next()){
                    try {
                    Float villeSurface = (Float) rs.getObject("ville_surface");

                        res.add(new CityDTO(rs.getString("ville_nom_reel")
                                            , rs.getString("ville_departement")
                                            , rs.getString("ville_code_postal")
                                            , (Integer)rs.getObject("ville_population_1999")
                                            , (Integer)rs.getObject("ville_population_2010")
                                            , (Integer)rs.getObject("ville_population_2012")
                                            , villeSurface == null ? (Double) null : new Double(villeSurface.doubleValue())
                                            , rs.getDouble("ville_longitude_deg")
                                            , rs.getDouble("ville_latitude_deg")
                                            , (Integer)rs.getObject("ville_zmin")
                                            , (Integer)rs.getObject("ville_zmax")));
                    }catch(Exception e){
                        System.err.println(e);
                    }
                }
            }catch (SQLException e){
                System.err.println(e);
            }
            return res;
        }
```

On lit des (références vers des) objets plutôt que des valeurs de types primitifs lorsque les colonnes peuvent contenir des `NULL`, auquel cas la référence retournées est nulle.

Il est aussi possible de tirer parti de la correspondance entre tables et classe, pour automatiser la persistance des objets d'un programme Java. Ceci grâce à [Java Persistance Api](https://fr.wikipedia.org/wiki/Java_Persistence_API).


<a id="org3d77a78"></a>

## Exemple de relation Many to Many, table d'associations

Pour le stockage de l'information concernant les codes postaux de chacune des villes, le format proposé (une colonne de type chaîne de caractères pouvant contenir une liste de codes postaux séparés par des '-', n'est ni pratique ni performant. On va écrire un programme implémentant la relation «Many to Many» par une table d'associations. Il s'agit d'une relation «Many to Many» car une ville peut avoir plusieurs codes postaux, mais un code postal peut être associé à plusieurs villes. Pour représenter cette association, on va créer deux tables :

-   une table `postalcodes` qui va contenir la chaîne de caractère du code postal et un identifiant.
-   une table `city_postalcode` qui va contenir les associations entre la table `cities` et la table `postalcodes`, avec seulement les deux colonnes `cities_pk` et `postalcodes_pk` ("pk" pour Primary Key). La clé primaire de cette table est constituée par ces deux colonnes.
