- [Manuels](#orgc5af08d)
  - [Manuel de déploiement](#org2b6e584)
  - [Manuel d'utilisation](#org16d4fe6)
  - [Manuel de développement](#org80265c3)
- [Code](#org5a538f3)
  - [Architecture](#org878e228)
  - [Durées de vie et portées](#orge1d9127)



<a id="orgc5af08d"></a>

# Manuels


<a id="org2b6e584"></a>

## Manuel de déploiement

Il faut rendre accessible sur/à partir du poste :

-   le programme
-   la/une base de données


### Déploiement du programme

Comment l'application sera-t'elle utilisée ?

-   **À partir d'Eclipse:** Dans ce cas, le 'déploiement' sera la recopie du répertoire contenant le projet, et son 'import' sous Eclipse ☹.
-   **En utilisant les classes compilées et éventuel fichier .properties:** Dans ce cas, on doit recopier les fichiers '.class' et la structure de répertoires / sous-répertoires correspondant aux *packages*.
-   **En utilisant un fichier .jar:** il suffit de recopier le fichier .jar.

Dans les deux derniers cas, comme les fichiers *.class* et *.jar* ne sont pas versionnés sous git, il faut les mettre à disposition. Par exemple dans le cadre d'une [release github](https://blog.github.com/2013-07-02-release-your-software/). Le manuel de déploiement doit alors indiquer quelles sont les versions (minimum) requises.

Il faut aussi penser aux dépendances, par exemple la bibliothèque de pilote JDBC pour Postgresql. Dans le cas d'une distribution de sources (utilisation d'Eclipse), `maven` prendra en charge le téléchargement automatiquement. Dans le cas de l'utilisation des fichiers .class compilés, il faudra que le fichier .jar du pilote soit dans le [CLASSPATH](https://en.wikipedia.org/wiki/Classpath_(Java)). Dans le cas d'un fichier .jar, il faudra choisir si l'on laisse (oblige à) utiliser un driver dans le *CLASSPATH* (comme précédemment), ou si l'on produit un *fat jar* (ou *uber jar*) (par exemple [avec maven](https://dzone.com/articles/creating-executable-uber-jar%E2%80%99s)).


### Déploiement de la base

Deux cas de figure :

-   le programme utilise une base déjà existante et accessible (par exemple [hébergée](http://elephantsql.com/). Le manuel de déploiement doit alors indiquer ses caractéristiques (URL, login, pass, ports utilisés).
-   le programme utilise une base spécifiquement crée. Le manuel de déploiement indique quel SGBDR est nécessaire et fourni les script SQL éventuellement nécessaire pour initialiser la base de données (une autre possibilité est que l'initialisation soit réalisée par le programme lui-même).


<a id="org16d4fe6"></a>

## Manuel d'utilisation


### Lancement du programme

Le manuel indique comment lancer le programme (cf. supra options de déploiement) et éventuellement comment paramétrer l'exécution (fichier *.properties*, variables d'environnement, arguments) par exemple pour l'adresse de la base et les login / mot de passe pour y accéder).


### Exécution

Le manuel indique comment interagir avec le programmes (écrans…).


<a id="org80265c3"></a>

## Manuel de développement


### Base de données

Suivant que la conception de la base de données a fait ou non partie du développement, le manuel indique les différents modèles (logique, conceptuel, physique, implémentation) selon leur pertinence (si le modèle est complexe, on aura besoin des modèles les plus abstraits pour ne pas être embrouillé par les détails des modèles plus concrets).

Les types de données et les contraintes sont justifiées, ainsi que les conventions de nommage (référence à la norme suivie).


### Code

Les éventuels packages et les classes sont présentées, notamment avec un ou plusieurs diagrammes de classe (UML).

Si possible, une documentation est générée avec [Javadoc](http://www.oracle.com/technetwork/articles/java/index-137868.html).

Si possible, les tests (et comment les lancer) sont expliqués.

La façon de générer le programme (par exemple un *.jar*, cf. déploiement) est expliquée.


<a id="org5a538f3"></a>

# Code


<a id="org878e228"></a>

## Architecture

Comment décomposer son code en classes ? L'objectif de la décomposition est principalement d'isoler en composants plus ou moins autonomes ce qui peut l'être, afin de limiter l'étendue de ce qui sera concerné par une éventuelle lors de la maintenance du code. Bien sûr, l'exercice est tellement limité qu'il n'y a pas vraiment d'enjeu et il faut faire preuve d'imagination pour mettre en œuvre ce qui ne sera nécessaire que pour un 'vrai' projet.

On peut par exemple isoler :

-   chacune des *entités* (membre d'un club de sport, article vestimentaire, client, ce qui est vendu,…) qui sont représentées dans la base (tables et lignes de ces tables) et manipulées par le programme (classes et objets instances de ces classes, dont les attributs correspondent aux colonnes).
-   Pour chacune de ces entités, ce qui permet d'interagir avec la table correspondante ([Data Access Object](http://www.oracle.com/technetwork/java/dataaccessobject-138824.html)).
-   le code qui manipule les entités pour réaliser les opérations voulues.
-   le code qui permet à l'utilisateur d'interagir avec le programme (*User Interface*).

Ainsi, toute modification de l'*implémentation* de l'une de ces classes n'aura pas d'impact sur le reste du code.


### Classes 'entités'

1.  Attributs

    Ces classes contiennent les attributs qui correspondent aux colonnes de la table correspondante. Il faut choisir les types correspondants, en se posant la question de la possibilité ou non de valeurs manquantes (`NULLABLE`). Si une valeur peut être manquante (`NULL`), on la représentera par un objet, ou plus exactement une référence qui pourra être nulle. On aura un attribut `id` correspondant à la clé primaire.

2.  Constructeurs

    On voudra faire un constructeur 'classique' qui prendra autant d'argument que la classe a d'attributs d'instance et les initialisera tous. Ce constructeur permettra de créer des objets lus dans la table. Mais pour créer de nouveaux objets, par exemple à partir de valeurs saisie par l'utilisateur/trice, on ne disposera pas de la valeur de l'identifiant. En effet, cette valeur (dans le cas qui nous intéresse d'une clé primaire de type `SERIAL`) est générée par la base de données lors de l'insertion. On aura donc un autre constructeur qui construira des objets au laissant l'identifiant en valeur manquante, avant l'insertion dans la base. Cette insertion devra mettre à jour la valeur de l'identifiant.


<a id="orge1d9127"></a>

## Durées de vie et portées


### Appels à .close

Tous les objets qui doivent être 'fermés' par un appel à une méthode `.close()` doivent être initialisés dans un [try with resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html) (ce qui impose une version de java supérieure ou égale à `1.7`, cf § déploiement) ou défaut avoir un appel à `.close()` dans un bloc `finally`. Ce la concerne aussi bien les objets manipulés à travers l'interface [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html) que les [java.sql.Statement](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html) ou (mieux !) [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html).


### Statement vs PreparedStatement

Pour éviter les [risques](https://xkcd.com/327/) d'[injection SQL](https://www.explainxkcd.com/wiki/index.php/Little_Bobby_Tables), on ne construira **JAMAIS** de requêtes SQL à partir de chaînes de caractères saisies par l'utilisateur/trice ! On utilisera [java.sql.PreparedStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/PreparedStatement.html) récupéré par un appel à [prepareStatement](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html#prepareStatement(java.lang.String)).


### Objet [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html)

Se pose le problème de la durée de vie de la connexion, et comment elle est partagée ou non et avec quelle portée.

Au minimum, une seule connexion doit être utilisée pour toutes les opérations SQL au sein d'une même *transaction*.

Au maximum, on sera tenté de réutiliser le même objet connexion dans tout le programme. Cependant, c'est sans doute une mauvaise idée dans le cas d'un programme qui peut tourner un temps indéterminé en attendant des entrées : le serveur de base de données prendra lui-même l'initiative de fermer la connexion au bout d'un certain temps si celle-ci est inactive (*idle*) !

Il est plus sûr de recréer une connexion à chaque fois que le programme traite une demande.
