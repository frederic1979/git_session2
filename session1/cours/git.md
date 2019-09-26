# Git

## C'est quoi git

Git est un **système de gestion de version**. Il permet **d'historiser** des fichiers texte (notamment du code source) en gardant la trace des changements qui ont été fait tout au long de l'histoire des fichiers. Il permet aussi aux développeur•euse•s de **partager** des fichiers et de **collaborer** en mettant en commun le code source sur des repositories **distants** (Github, Gitlab, Bitbucket, ...). Lorsque les fichiers sont partagés entre développeur•euse•s il peut y avoir des **conflits** lorsque les mêmes personnes travaillent sur les mêmes fichiers. Git permet **d'identifier** et de **résoudre** les conflits.

Dans votre vie de développeur•euse git sera un outil puissant et indispensable !

## Comment démarrer avec git

Lorsque vous allez coder, vous écrirez du code dans des fichiers texte (du Java, du Python, du HTML, ...). Ces fichiers seront rangés dans un répertoire que vous créerez pour votre projet. Afin d'historiser votre code avec git, vous **devez** _(oui, c'est un ordre)_ dès le démarrage de votre projet, même si vous êtes tout•e seul•e, créer un repository personnel avec la commande :

```git
git init
```

Cette commande va créer un dossier caché dans votre répertoire qui contiendra toutes les informations nécessaire à git pour historiser proprement votre projet.

## Les grands principes

### Les arbres de git

#### L'espace de travail

Tout le code que vous allez écrire va donc se trouver dans votre **espace de travail** (ou dossier). Par défaut, si vous avez fait un `git init`, git considère que **tous les fichiers** que vous allez créer sont à historiser. Dès le démarrage vous pouvez lui indiquer s'il y a des fichiers à **ignorer** grâce à un fichier à mettre à la racine de votre projet nommé `.gitignore`. Dans ce fichier, il vous suffira de nommer les fichiers que vous voulez ignorer. Vous verrez avec l'expérience qu'un bon nombre de fichiers peuvent être ignorés. Vous pourrez vous aider de ce petit utilitaire bien sympathique pour créer vos fichiers `.gitignore` : [gitignore.io](https://www.gitignore.io/).

#### L'index

Lorsque vous travaillerez sur votre code, vous allez certainement modifier plusieurs fichiers. Parfois vous jugerez nécessaire de ne **pas tous** les historiser en **même temps**. Grâce à l'index, vous pourrez choisir lesquels historiser. Lorsque vous aurez besoin de choisir, il vous suffira d'utiliser la commande :

```git
git add <nom-du-fichier-a-historiser>
```

et votre fichier sera ajouté à l'index.

#### HEAD

Une fois que vous avez choisi les fichiers à historiser en les ajoutant à l'index. Il vous restera à valider les changements. Pour valider les changements vous utilserez la commande :

```git
git commit -m "correction du bug bloquant #0012B"
```

`commit` permet de créer une nouvelle **photo** de votre code.

Si l'on veut imager ces trois concepts, on peut imaginer un mariage :

- **L'espace de travail** c'est **le lieu** où sont tous les invités
- **L'index**, c'est lorsque le photographe **appelle** la famille de la mariée
- **Le commit**, c'est lorsqu'il prend **la photographie**.

### Le repository distant

Jusqu'ici, vous avez travaillé **en local**. Toutes les **versions** de votre code sont sur votre machine. Si votre disque dur explose, tout est perdu et vos collègues ne veront jamais votre travail. Vous allez avoir besoin d'un repository **distant** pour **partager et sauvegarder** durablement votre code.

Pour cela vous aurez besoin de créer un repository distant (sur Github par exemple ==> [Tutoriel Github](https://guides.github.com/activities/hello-world/)). Une fois votre repository créé vous aurez son adresse et vous pourrez **lier** votre reposiroty local à votre repository distant avec la commande :

```git
git remote add origin <url-de-votre-repo-distant>
```

Avec cette commande, on lie notre repository distant que l'on nomme _origin_ (c'est une convention pour les repositories distants mais on peut l'appeler autrement) avec notre repository local.

Une fois cette action réalisée (une seule fois suffit), vous pourrez **pousser** vos versions vers le repository distant avec la commande :

```git
git push origin master
```

Avec cette commande, on pousse nos versions sur _origin_ qui est notre repository distant. En fin de commande, on remarque le mot _master_ qui est la **branche principale** d'un repository. On détaille cette notion de branche ci-dessous.

### Les branches

Les branches permettent de créer des espaces de travail **différents** ayant une base de code commune.

Imaginons que votre logiciel soit en production, le code qui a été compilé pour être dans l'application est le code de la branche _master_, c'est la **racine** de votre code. On vous demande de développer une **nouvelle fonctionnalité**. Vous commencez à la développer sur la branche _master_, vous poussez vos commits et ça avant plutôt bien. Mais un client vous appelle pour vous dire qu'il y a un **bug bloquant** et qu'il faut **refaire une version** de votre application. Damned! Vous n'avez pas fini votre nouvelle fonctionnalité, mais le code est déjà sur _master_ et vous êtes dans la mouise pour corriger le bug bloquant sans inclure les changements de la nouvelle fonctionnalité.

Cela peut être évité si vous créez une branche spéciale pour votre nouvelle fonctionnalité ! En utilisant la commande :

```git
git checkout -b nouvelle-fonctionnalite-top-moumoutte
```

Vous avez maintenant la possibilité de travailler avec deux versions **différentes** de votre code. Celle de la **branche** _master_ qui ne contiendra pas les changements que vous ferez pour la nouvelle fonctionnalité, et celle de la **branche** _nouvelle-fonctionnalite-top-moumoutte_ qui ne contiendra pas les changements faits en urgence pour corriger le bug bloquant.

La commande `checbkout` permet de **changer** de branche. L'option `-b` permet de **créer** la branche. Si l'on souhaite revenir sur la branche _master_, il suffit d'exécuter la commande :

```git
git checkout master
```

Evidemment, si vous ajoutez une super fonctionnalité, vous allez vouloir la répercuter sur la branche _master_ lorsqu'elle sera prête. Si vous êtes positionné sur la branche _master_, vous pourrez le faire grâce à la commande :

```git
git merge nouvelle-fonctionnalite-top-moumoutte
```

## Pour mieux comprendre

Voici les commandes de survie de git. Il y en a beaucoup d'autres que nous serons amené à rencontrer petit à petit pendant la formation. Pour bien démarrer

[Un guide de survie pour les débutant•e•s](https://rogerdudler.github.io/git-guide/index.fr.html)

[Un tutoriel pour comprendre les arbres](https://ndpsoftware.com/git-cheatsheet.html)

[Un tutoriel pour comprendre les branches](https://learngitbranching.js.org/)
