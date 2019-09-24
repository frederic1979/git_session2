# Le système d'exploitation Linux

Avant de parler du système d'exploitation Linux, il convient de définir quelques termes essentiels : 

- Le **terminal**
- La **donnée**
- Le **logiciel**
- Le **système d'exploitation**

## Terminologie

### Définition d'un terminal

Un système d'exploitation sans terminal n'a pas grand intéret. Nous utilisons tous un ou plusieurs **terminaux**. Vous avez sûrement un smartphone, un ordinateur ou peut-être une tablette. Ce sont des terminaux, des **extrémités** d'un réseau informatique. Pour que les terminaux fonctionnent, plusieurs **composants** essentiels sont nécessaires :

- Un ou plusieurs processeurs pour réaliser les **calculs**
- De la mémoire vive pour stocker les informations **transitoires**
- De la mémoire de stockage pour retenir les informations sur le **long terme**
- Une ou plusieurs carte•s reseau pour pouvoir **communiquer** avec d'autres terminaux.

### Définition d'une donnée

Une donnée est la **représentation numérique** d'une information (une photo, un morceau de musique, ...) sous la forme d'une suite de bits. Une donnée se caractérise par plusieurs attributs :

- Un format : la **convention d'interprétation** par le terminal (UTF-8, jpeg, ...)
- Une taille : le **nombre de bits** composant la données
- Un conteneur : le fameux **fichier**

### Définition d'un logiciel

Un logiciel est une suite **d'instructions interprétables** par un terminal. Les logiciels sont sous **licence** (libre ou propriétaire) et sont très souvent identifiés par une **version**.

### Définition d'un système d'exploitation

Le système d'exploitation est le **chef d'orchestre** de tous les composants d'un terminal. C'est **LE** logiciel qui gère toutes les ressources d'un terminal. Vous en connaissez certainement quelques uns :

- Windows 10
- macOS Mojave
- Android Oreo
- iOS 12
- Ubuntu 18.04 LTS

## Linux

La particularité de Linux est d'être un **noyau** (la suite de programme permettant d'intéragir avec les composants d'un terminal). Il est souvent confondu avec un système d'exploitation complet car de nombreuses **distributions** portent le nom de Linux. Les distributions sont les systèmes d'exploitation complets (noyau + logiciels de base pour intéragir avec le terminal). De nombreuses distributions sont basées sur le noyau Linux (Ubuntu, Linux Mint, Debian, ...).

Linux est **open source**. Cela veut dire que le code informatique écrit pour créer le logiciel est visible pour tout le monde. Les distributions qui sont basées sur Linux sont donc elles aussi open source. Cela ne veut pas forcément dire que les distribtions sont **gratuites**. Open source **ne veut pas** dire gratuit.

Il est intéressant de voir à quel point les différentes distributions Linux sont variées : [Infographie des distributions](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg).

Aujourd'hui, les distributions Linux sont assez peu représentées sur les terminaux pesonnels mais sont largement utilisées dans le cloud : [Statistiques Cloud Market](https://thecloudmarket.com/stats), [Statistiques w3techs](https://w3techs.com/technologies/overview/operating_system/all).

C'est pour cette raison que nous allons utiliser Linux pendant la formation. Lorsque vous travaillerez en entreprise, il y a de fortes chances que vous ayez à configurer ou déployer vos applications sur des serveurs fonctionnant sous Linux.

## Le bash

Sous Linux, un outil **incontournable** du développeur est le [bash](https://fr.wikipedia.org/wiki/Bourne-Again_shell). C'est un interpreteur en ligne de commande. Il permet d'exécuter des actions sur le système de fichier, de controler différents logiciels, de configurer le réseau, ... Cela peut paraître étrange de vouloir utiliser des lignes de commandes aujourd'hui où les interfaces graphiques sont très bien développées. Pourtant c'est encore beaucoup utilisé. En effet c'est souvent beaucoup plus efficace pour certaines actions. 

### Les commandes de survie

#### Chercher de l'aide

`man _commande_` permet d'afficher l'aide de la commande. On peut aussi utiliser `_commande_ --help`.

#### Se localiser sur le système de fichier et naviguer

`pwd` pour _Print Working Directory_ permet d'afficher dans la console notre emplacement dans le système de fichier.

`ls` permet d'afficher le contenu d'un dossier dans lequel on se trouve.

`cd _localisation_` permet de changer d'emplacement dans le système de fichier.

#### Jouer avec les fichier

`touch _fichier_` permet de créer un nouveau fichier.

`cat _fichier_` permet d'afficher tout le contenu d'un fichier directement dans la console.

`more _fichier_` permet d'afficher le contenu d'un fichier dans la console de manière intelligente (on peut faire défiler le fichier).

`head _fichier_` permet d'afficher les premières lignes d'un fichier (par défaut les x premières).

`tail _fichier_` permet d'afficher les dernières lignes d'un fichier (par défaut les x dernières).

`cp _fichier1_ _fichier2_` permet de copier le _fichier1_ à l'emplacement _fichier2_.

`mv _fichier1_ _fichier2_` permet de déplacer le _fichier1_ à l'emplacement _fichier2_.

`rm _fichier1_` permet de supprimer le _fichier1_.

#### Les permissions

Il faut savoir que chaque fichier est associé à un utilisateur **propriétaire**. De plus, les fichiers et les répertoires ont des **permissions**. Les utilisateurs peuvent lire, écrire ou exécuter un fichier et lire ou écrire dans un répertoire. Ainsi, plusieurs utilisateurs d'un même terminal ne peuvent pas forcément tous faire la même chose avec le même fichier. Les droits peuvent être définis au niveau de l'utilisateur, du groupe auquel appartient l'utilisateur ou du reste du monde.

Pour en savoir plus : [La documentation Ubuntu](https://doc.ubuntu-fr.org/droits)

Les commandes importantes à connaître sont `chown` pour changer le propriétaire d'un fichier et `chmod` pour modifier les droits sur un fichier.

Pour en savoir plus : [La documentation Ubuntu](https://doc.ubuntu-fr.org/permissions).

#### La connexion à distance

Afin de vous connecter à distance aux différents serveurs qui hébergeront vos applications, vous aurez certainement à utiliser le protocole `ssh`. Nous n'utiliserons peut-être pas la commande pendant la formation mais elle est à découvrir sur [La documentation Ubuntu](https://doc.ubuntu-fr.org/ssh).

#### Pour aller plus loin

[Le kit de survie](https://www.commentcamarche.net/faq/8386-kit-de-survie-linux)
