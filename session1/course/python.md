# Découvrons Python

## Dessine moi un Python

Python est un langage de programmation. Nous allons ici découvrir les bases de son utilisation.

Un langage de programmation est destiné à permettre l'écriture et la manipulation de structures de données par un terminal informatique (ordinateur, téléphone, ...). Comme tout langage de programmation, Python possède un **vocabulaire** (des mots clés) et des **règles de grammaire** (comment agencer les mots clés).

Python est un langage **interprété**, les mots clés que nous allons utiliser dans nos lignes de code seront lues par un **interpreteur** qui "dira quoi faire à notre machine".

Il est beaucoup utilisé dans le monde de la data car il possède de nombreuses bibliothèques mathématiques (morceaux de code réutilisables) accessibles pour les développeurs.

Dans ce cours nous verrons comment créer un unique **script** Python. Il s'agira d'écrire une suite d'instructions dans un seul et même **fichier** Python. Nous passerons ensuite à l'interpréteur Python le fichier en **paramètre**. L'interpréteur se chargera de lire les instructions de haut en bas et de les exécuter les unes après les autres.

Avant toute chose, il convient de parler des commentaires ! C'est certainement une des choses les plus importantes que l'on écrit lorsque l'on code. Ce sont des lignes de code qui ne seront pas interprétées mais qui donnent des indications primordiales pour les programmeurs qui liront le code (y compris vous dans quelques mois / années).

```python
# Voici comment j'écris un commentaire en Python : en démarrant ma ligne de code par le caractère #
# C'est vraiment très important de documenter son code en mettant des bons commentaires pour les futurs développeur•euse•s
# J'espère que vous le ferez !
```

## Variable et type de données

En Python, nous allons pouvoir définir des **variables**. Ce sont des blocs de la mémoire de l'ordinateur que le programme va réserver pour y stocker des données (un age, un prénom, la liste des numéros gagnants du loto, votre adresse IP, ...). Chaque variable aura un **type de données** associé (un age sera un nombre, un prénom sera une chaîne de caractères, ...)

Pour **déclarer** une variable en Python il suffit de donner un nom à notre variable et de lui donner une valeur.

```python
age = 30
prenom = "Jules"
```

### Les nombres

Deux grand types de nombre nous seront utiles : les `int` qui représentent les nombres entiers et les `float` qui représentent les nombres décimaux.

```python
# Mon age
age = 30

# Ma taille en cm
taille = 184.5
```

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/introduction.html#numbers)

### Les chaînes de caractères

Afin de stocker du texte (un prénom, un nom, une phrase, ...) nous utiliserons les `string` qui représentent les chaînes de caractères. Il y a deux méthodes pour déclarer un `string` (avec guillemets simples ou doubles):

```python
prenom = "Jules"
nom = 'Jules'
```

Parfois on peut avoir envie d'utiliser des **guillements** dans la chaîne de caractères. Dans ce cas on peut procéder comme suit :

```python
presentation = "Je m'appelle Jules"
citation = '"Bienvue à Simplon!" - Jonathan.'
```

Parfois on peut avoir envie de combiner les deux :

```python
citation = '"Je suis le pape et j\'attends ma soeur" - Odile de Ray.'
```

Dans cette dernière citation, j'ai besoin **d'échapper** le guillement simple afin qu'il ne soit pas interprété comme la fin de la chaîne de caractères. On utilise dans ce cas le caractère `backslash`.

On peut aussi avoir besoin d'écrire une chaine de caractères qui contient plusieurs lignes de texte. Dans ce cas, deux solutions : utiliser le caractère spécial `\n` pour indiquer un retour à la ligne ou utiliser le commentaire multiligne.

```python
presentation = "Je m'appelle Jules\nJ'ai 30 ans."
passions = """- Aviron
- Self-Hacking
- The lord of the ring"""
```

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/introduction.html#strings)

## Opérateurs

@Joss'

## Booléen et conditions

@Joss'

## Les fonctions

@Jules

## Tableaux

@Joss'

## Boucles

@Joss'

## Entrées / Sorties

@Jules