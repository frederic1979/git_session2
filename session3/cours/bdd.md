# Les bases de données relationnelles

## Un peu de vocabulaire

Avant toute chose, il convient de définir ce qu'est une donnée. Une **donnée** est une **information relative à un objet**. On peut prendre l'exemple de la couleur d'un pull. Il s'agit d'une donnée qui peut prendre la valeur _rouge_, _bleu_, _noir_, _jaune_, _vert_, _rose_ ... Dans que cas là, on dira que la donnée est **qualitative**, car elle me permet de qualifier un objet. On peut aussi avoir des données **quantitatives**. Prenons l'exemple du nombre d'apprenant•e•s d'une promotion Simplon. Cette donnée peut prendre une valeur entière numérique et strictement positive (entre 8 et 20 dans le cas des formations Dev Web).

Une relation est un **lien** qui existe entre des choses. On peut reprendre l'exemple de la couleur d'un pull, mais cette fois en spécifiant la couleur de _mon_ pull. Dans ce cas on peut noter le lien entre un objet pull et une personne.

Une **base de données relationnelle** est un système informatique qui permet de stocker des données tout en permettant de représenter les liens qui existent entre ces données. On pourrait par exemple stocker des _personnes_ et des _pulls_ et représenter les liens entre ces deux différentes choses (un pull peut appartenir à une seule personne, une personne peut avoir plusieurs pulls).

Les bases de données sont exploitables grâce à des logiciels : les **systèmes de gestion de base de données relationnelle**. Ils permettent de créer des bases de données, de stocker des données, de récupérer des données, ...

## Un peu d'histoire

Depuis la création des premiers systèmes informatiques, les **données** sont au coeur du réacteur. Les premières machines avaient très souvent un unique but et traitaient un type de données bien précis. Un exemple d'une toute première conçu pour exploiter des données de type texte est le [Colossus](https://cryptomuseum.com/crypto/colossus/index.htm) (un système conçu pour déchiffrer les messages que s'envoyaient les hauts dirigeants allemands pendant la seconde guerre mondiale).

Le premier ordinateur entièrement électronique est [l'ENIAC](https://fr.wikipedia.org/wiki/ENIAC). Il permettait de résoudre tous les problèmes calculatoire (additions, soustractions, multiplications et divisions avec des données numériques). On appelait d'ailleurs souvent les premières machines informatiques des **calculateurs**. Ces machines avaient été inventées pour effectuer les calculs trop complexes à faire à la main. Dans le cas de l'ENIAC, il s'agissait de réaliser des calculs pour réaliser les tirs balistiques.

Le besoin de stocker les données et de les mettre en relation entre elles a très vite été rencontré. Les premières données stockées le furent de manière hierarchique. Cependant il pouvait être difficile de relier les données entre elles et d'autres problèmes (comme la redondance des données) pouvait rendre le traitement des données laborieux.

Dans les années 1970 l'anglais [Edgar Codd](https://history-computer.com/ModernComputer/Software/Codd.html) propose un système pour gérer les données sous forme de tables pouvant être liées entre elles. Chaque table doit représenter un type d'objet et dans les tables, les colonnes permettent de définir les attributs de l'objet et les lignes seront une instance d'un objet.

Si l'on prend à nouveau l'exemple des personnes et des pulls, on pourrait avoir deux tables, une table `personne` ainsi qu'une table `pull`. La table `personne` pourrait avoir les colonnes `identifiant`, `nom` et `prénom` et la table pull avoir une colonne `identifiant`, `couleur`, `taille` et `ID du Propriétaire`. On pourrait avoir les lignes suivantes :

`Personne` :

| Identifiant | Nom      | Prénom     |
|-------------|----------|------------|
| 1           | Grand    | Jules      |
| 2           | Hugueney | Bernard    |

`Pull` :

| Identifiant | Couleur  | Taille     | ID du Propriétaire |
|-------------|----------|------------|--------------------|
| 1           | Vert     | L          | 2                  |
| 2           | Rouge    | M          | 1                  |

Grâce à ce modèle, on peut stocker des données du même type dans une même table et faire des relations entre les tables grâce aux identifiants (plus de détails dans les sections à venir). On peut utiliser **l'algèbre relationnelle** pour effectuer des opérations sur les données comme des **sélections, des jointures, des unions, ...**.

## Le travail du•de la programmeur•euse

### Concevoir la base de données

Lors de la conception d'une base de données, on se base très souvent sur un modèle de données. On peut avoir défini un diagramme de classe objet en UML, on peut avoir créé un modèle conceptuel de données, ... Bref, on a des classes et des relations (ou des entités et des associations).

L'objectif est de passer de ce modèle à une base de données reprenant ce modèle dans un schéma (plan des relations entre tables).

Lors de la conception, on doit veiller à :

- garantir l'atomicité des données (un donnée atomique dans chaque colonne, par exemple pour un utilisateur on définit les colonnes : `nom`, `prénom` et `téléphone` et pas `nom complet` et `téléphone` car cela nous empècherait d'effectuer des opérations différentes sur les _noms_ et les _prénoms_).
- ne pas mélanger les données (une table pour chaque type de donnée : `Voiture`, `Client`, ...)
- éviter la redondance des données (ne pas définir une même donnée dans deux tables différentes)

#### La création des tables

Lors de la création des tables, afin de pouvoir appliquer les opérations d'algèbre relationnelle, on doit définir des clés.

##### Définition des clés primaires

Une **clé primaire** est un identifiant unique d'un enregistrement (ou ligne) d'une table. Cela peut-être n'importe quelle information permettant d'identifier une donnée. La base de données interdira ensuite toute insertion dans la table d'une donnée ayant la même clé. Pour une donnée de type `personne` on pourrait imaginer utiliser le couple `nom` et `prénom` mais cela voudrait dire que des personnes ayant les mêmes _noms_ et _prénoms_ ne pourraient pas être stockées dans la même table. On pourrait alors penser à l'information _email_ qui doit en théorie être unique. Cependant en pratique on utilise très souvent un _identifiant_ qui est un nombre entier s'incrémentant automatiquement au fur et à mesure des insertions en table.

`Personne` :

| Identifiant | Nom      | Prénom     |
|-------------|----------|------------|
| 1           | Grand    | Jules      |
| 2           | Hugueney | Bernard    |

##### Définition des clés étrangères

Les **clés primaires** permettent d'identifier de manière unique un enregistrement. On peut donc les utiliser pour créer des **relations** entre différentes données. Lorsqu'on utilise la valeur d'une **clé primaire** identifiant un enregistrement dans une autre table, on parle de **clé étrangère**. Par exemple si j'ai une table `personne` et une table `pull` et que je veux créer une relation entre les deux tables, je vais faire référence à la table `personne` dans la table `pull` grâce à une clé étrangère dans la table `pull`.

`Pull` :

| Identifiant | Couleur  | Taille     | ID du Propriétaire |
|-------------|----------|------------|--------------------|
| 1           | Vert     | L          | 2                  |
| 2           | Rouge    | M          | 1                  |

##### Définition de contraintes

On peut aussi appliquer des contraintes sur nos données afin d'assurer leur cohérence (on peut par exemple refuser des dates de naissances ulterieures à la date du jour, refuser les valeurs négatives pour une donnée de type salaire).

### Exploiter la base de données

#### Création de la base de données

#### Exploiter les données

#### Insérer des données

#### Mettre à jour des données

#### Selectionner des données

##### Selection simple

##### Jointure

#### Supprimer des données

## Les objectifs SGBDR

Les bases de données relationnelles permettent donc de représenter des entités sous formes de tables. Elles ont aussi pour objectif de :

- Assurer la confidentialité des données (avec un contrôle d'accès)
- Assurer les accès concurents aux données
