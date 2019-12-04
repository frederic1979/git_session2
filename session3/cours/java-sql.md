- [Types d'utilisations de bases de données](#org8003c57)
- [Utilisation de SGBDR en Java : préliminaires](#orga0c1627)
  - [Chargement de drivers](#orgb9dc8d8)
  - [Établissement de la connection au SGBDR](#org2a61ce3)
- [Utilisation de SGBDR en Java : requêtes SQL](#org4cb2e4f)
  - [java.sql.Statement](#org322675b)
  - [java.sql.PreparedStatement](#org408eedd)
  - [Lecture des résultats d'une requête SELECT](#orgfb99be4)
  - [Exemple de relation Many to Many, table d'associations](#org1572399)



<a id="org8003c57"></a>

# Types d'utilisations de bases de données

Il y a plusieurs façons d'utiliser des bases de données avec un logiciel écrit en Java :

-   **Embarquée:** Lorsque le programme de gestion de bases de données est écrit en Java, il peut être directement intégré en tant que bibliothèque Java. Dans ce cas, on peut même utiliser une "base de données" virtuelle en mémoire. Si l'accès aux données est alors très rapide, il n'y a évidemment pas de durabilité, donc ceci est plutôt réservé aux situations de tests.
-   **Serveur (local) et tables dédiés:** Le serveur est utilisé pour permettre la durabilité des entités manipulées par le logiciel.
-   **Serveurs (distant) et tables partagés:** Le logiciel est utilisé pour manipuler des entités déjà existantes.


<a id="orga0c1627"></a>

# Utilisation de SGBDR en Java : préliminaires

Les SGDBR et leurs drivers Java permettent différents niveaux de fonctionnalités. Dans un soucis de simplicité et de compatibilité maximale, on ne s'intéresse ici qu'aux fonctionnalités les plus basiques dont la disponibilité est garantie. En cas de besoin, et si le SGDBR est connu et fixé, on pourra utiliser [des fonctionnalités plus avancées](https://docs.oracle.com/javase/tutorial/jdbc/basics/retrieving.html).


<a id="orgb9dc8d8"></a>

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

-   **Exercice:** Créer un projet Maven avec une dépendance sur la bibliothèque de driver Postgresql et une autre sur la bibliothèque de driver H2. Écrire un programme qui charge ainsi le driver à l'exécution, suivant ce qui est passé en argument :


<a id="org2a61ce3"></a>

## Établissement de la connection au SGBDR

La connection au SGDBR est matérialisée par un objet instance d'une classe implémentant l'interface [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html) . Cette connection peut être en [mode autocommit ou non](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#getAutoCommit()). On récupère cet objet par un appel à la méthode [java.sql.DriverManager.getConnection()](https://docs.oracle.com/javase/7/docs/api/java/sql/DriverManager.html#getConnection(java.lang.String,%20java.lang.String,%20java.lang.String)). Par exemple, si les URL, login et mot de passe sont stockés dans une `Map<String,String> env` et assocés aux clés `"URL"`, `"USER"` et `"PASS"` :

```java
Connection conn= DriverManager.getConnection(env.get("URL"), env.get("USER"), env.get("PASS"));
```

L'url étant de la forme "jdbc:SGBD\_NAME://DBSERVER\_NAME:DBSERVER\_PORT/DATABASE\_NAME".

Il faudra s'assurer que la connection sera fermée à un appel à la méthode [close()](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#close()). On remarque que l'interface `java.sql.Connection` hérite de l'interface `java.lang.AutoClosable`, ce qui implique donc qu'on peut faire l'initialisation dans un bloc `try(){}` (dit «try with resources»). Attention : cette méthode `.close()` peut elle-même lancer une [SQLException](https://docs.oracle.com/javase/7/docs/api/java/sql/SQLException.html) qu'il faut donc aussi gérer.

On passera l'objet connection aux différentes méthodes qui s'en serviront pour interagir avec le SGBDR.


<a id="org4cb2e4f"></a>

# Utilisation de SGBDR en Java : requêtes SQL

Il y a deux façons de faire exécuter des requêtes SQL en Java, suivant qu'on utilise des [java.sql.Statement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html) ou des [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html).


<a id="org322675b"></a>

## java.sql.Statement

On commence par créer l'objet par un appel à [createStatement()](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#createStatement()) sur l'objet qui implémente l'interface `Connection`. Cet objet nouvellement créé devra lui aussi être fermé par un appel à sa méthode [close()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#close()). Comme il implémente l'interface `AutoCloseable`, on peut créer l'objet dans un `try(){}` («try with resources»).

Ensuite, on peut appeler sur cet objet l'une des méthodes suivante :

-   [execute(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#execute(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour un booléen indiquant si l'exécution s'est déroulée sans erreur ou non.
-   [executeUpdate(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeUpdate(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour le nombre de lignes modifiées (comme son nom l'indique, on utilise cette méthode pour des commandes SQL `UPDATE`).
-   [executeQuery(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeQuery(java.lang.String)) pour exécuter la commande SQL passée en paramètre, en ayant en valeur de retour un objet implémentant l'interface [java.sql.ResultSet](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html) qui permettra de récupérer les résultat d'une commande SQL `SELECT`.

De plus, si l'on veut exécuter plusieurs commandes SQL en une seule fois, pour des raisons de performance, on peut à la place utiliser la méthode [addBatch(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#addBatch(java.lang.String)) pour chacune des commandes, puis déclencher l'exécution de toutes celles-ci par un appel à [executeBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeBatch()).

Souvent, la commande SQL à exécuter dépend de valeurs qui ne sont connues qu'à l'exécution, par exemple les données à ajouter dans un `INSERT` ou des critères d'une clause `WHERE`. Il est possible de construire dynamiquement la commande SQL en concaténant des chaînes de caractères mais il faut alors faire très attention au risque d'[injection SQL](https://fr.wikipedia.org/wiki/Injection_SQL). Même sans utilisateurs hostiles, il faut de toutes façons prendre en compte l'échappement des caractères spéciaux dans une chaîne de caractères. Par exemple, le guillemet simple, utilisé souvernt pour l'apostrophe, doit être remplacé par deux guillemets simples pour éviter qu'il soit interprété comme la fin de chaîne. On peut faire pour cela un appel comme ceci : `.replaceAll("'","''")`.

Il est cependant préférable d'utiliser des [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html) pour ne pas avoir à gérer soi-même les arguments.


<a id="org408eedd"></a>

## java.sql.PreparedStatement

Toujours à partir de l'objet implémentant l'interface [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html), on peut utiliser la méthode [prepareStatement(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#prepareStatement(java.lang.String)) pour créer un objet implémentant l'interface [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html). La chaîne de caractère passée en argument contient le code de la commande SQL avec des '?' à la place des arguments de la commande. Par exemple, pour insérer une nouvelle ligne dans notre table `city`, on pourra utiliser :

```java
String insertCmd= "INSERT INTO cities VALUES(DEFAULT, ?, ?, ?);";
try(PreparedStatement stmt= conn.prepareStatement(insertCmd)){
}
```

Le `DEFAULT` permet de laisser la base de données attribuer la valeur de la clé primaire.

Comme pour la création d'un [java.sql.Statement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html), on peut (devrait ?) utiliser un *try with resources* parce que l'objet créé implémente l'interface `java.lang.AutoCloseable`.

Ensuite, on peut utiliser sur cet objet les méthodes `setXXX()` comme [setDouble(int parameterIndex, double parameterValue)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setDouble(int,%20double)) ou [setString(int parameterIndex, String parameterValue)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setString(int,%20java.lang.String)) pour donner des valeurs à chacun des paramètres représentés par un '?' dans la chaîne passée en argument de [prepareStatement(String sql)](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#prepareStatement(java.lang.String)). Attention ! Les `parameterIndex` commencent à 1 et non à 0. Si l'on veut insérer une valeur manquante `NULL`, il faut utiliser la méthode [setNull(int parameterIndex, int sqlType)](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#setNull(int,%20int)). L'argument `sqlType` étant l'une des constantes nommées définies dans la classe [java.sql.Types](https://docs.oracle.com/javase/7/docs/api/java/sql/Types.html).

Ensuite, une fois que tous les arguments on reçu une valeur, on peut appeler l'une des méthodes [execute()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#execute()), [executeQuery()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeQuery()) ou [executeUpdate()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeUpdate()). On peut aussi créer un batch de plusieurs commandes à executer à l'aide des méthodes [addBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#addBatch()) et [executeBatch()](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeBatch()).


<a id="orgfb99be4"></a>

## Lecture des résultats d'une requête SELECT

Lorsque l'on exécute une requête `SELECT`, on utilise la méthode [executeQuery()](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html#executeQuery()) qui retourne un objet implémentant l'interface [java.sql.ResultSet](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html). Cet objet permet de récupérer chacunes des données de chacune des lignes correspondant à la requête. Pour passer à la ligne suivante en testant s'il y en a une, on utilise la méthode [next()](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#next()) (le plus souvent comme condition de continuation dans une boucle `while()` pour traiter toutes les lignes de la première à la dernière). Ensuite, pour chacune des lignes (à l'intérieur de la boucle, donc), on peut récupérer la valeur de chacune des colonnes avec des appels aux méthodes [getDouble(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getDouble(java.lang.String)), [getInt(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getInt(java.lang.String)), [getLong(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getLong(java.lang.String)), [getString(String colName)](https://docs.oracle.com/javase/7/docs/api/java/sql/ResultSet.html#getString(java.lang.String)) et autres. Il est aussi possible de passer des numéros de colonne en argument plutôt que d'utiliser les noms, mais il faut alors se souvenir non seulement de l'ordre des colonnes dans le resultat, mais aussi que leur numérotation commence à 1 et non à 0. Toujours dans un soucis de plus grande compatibilité avec tous les drivers JDBC disponibles, mais aussi dans un soucis de performance, il est préférable de se contenter de lire les lignes les unes après les autres et pour chaque ligne et de ne lire les données qu'une seule fois pour une instance de `ResultSet` donnée.

Par exemple, pour afficher le contenue d'une table `city` contenant des communes avec leur latitude et longitude, on pourrait écrire le code suivant :

```java
try (Statement stmt = conn.createStatement()) {
    ResultSet rs = stmt.executeQuery("SELECT id, name, latitude, longitude from city");
    while (rs.next()) {
	try {
	    System.out.println(String.format("id: %d, name: %s, latitude: %f, longitude: %f",
					     rs.getLong("id"),
					     rs.getString("name"),
					     rs.getDouble("latitude"),
					     rs.getDouble("longitude")));
	} catch (Exception e) {
	    System.err.println(e);
	}
    }

} catch (SQLException e) {
    e.printStackTrace();
}

```

On lit des (références vers des) objets plutôt que des valeurs de types primitifs lorsque les colonnes peuvent contenir des `NULL`, auquel cas la référence retournées est nulle.

-   **Exercice:** Écrire un programme qui afficher le contenu d'une table `city` contenant des communes avec leur latitude et longitude. Vous pouvez créer une telle table en local, mais aussi utiliser une table `city` disponible sur le serveur `horton.elephantsql.com` au port `5432` avec comme login `vnzaekhx` et comme mot de passe `oWN4ryvxxdjYWsko1u3WTW23k6yB7bM9`.
-   **Exercice:** Écrire un programme qui remplisse une table d'une base de données locale à partir du fichier `Communes.csv` qui avait été donné lors de la session précédente.
-   **Exercice:** Écrire un programme qui remplisse une table d'une base de données locales à partir des donnés mises à disposition par [données mises à disposition par Tony Archambeau](http://sql.sh/736-base-donnees-villes-francaises).


<a id="org1572399"></a>

## Exemple de relation Many to Many, table d'associations

Pour le stockage de l'information concernant les codes postaux de chacune des villes, le format proposé (une colonne de type chaîne de caractères pouvant contenir une liste de codes postaux séparés par des '-', n'est ni pratique ni performant. On va écrire un programme implémentant la relation «Many to Many» par une table d'associations. Il s'agit d'une relation «Many to Many» car une ville peut avoir plusieurs codes postaux, mais un code postal peut être associé à plusieurs villes. Pour représenter cette association, on va créer deux tables :

-   une table `postalcodes` qui va contenir la chaîne de caractère du code postal et un identifiant.
-   une table `city_postalcode` qui va contenir les associations entre la table `cities` et la table `postalcodes`, avec seulement les deux colonnes `cities_pk` et `postalcodes_pk` ("pk" pour Primary Key). La clé primaire de cette table est constituée par ces deux colonnes.
