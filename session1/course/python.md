# Découvrons Python

## Dessine moi un Python

Python est un langage de programmation. Nous allons ici découvrir les bases de son utilisation.

Un langage de programmation est destiné à permettre l'écriture et la manipulation de structures de données par un terminal informatique (ordinateur, téléphone, ...). Comme tout langage de programmation, Python possède un **vocabulaire** (des mots clés) et des **règles de grammaire** (comment agencer les mots clés).

Python est un langage **interprété**, les mots clés que nous allons utiliser dans nos lignes de code seront lues par un **interpreteur** qui "dira quoi faire à notre machine".

Il est beaucoup utilisé dans le monde de la data car il possède de nombreuses bibliothèques mathématiques (morceaux de code réutilisables) accessibles pour les développeurs.

Dans ce cours nous verrons comment écrire et exécuter du Python. Deux méthodes différentes s'offrent à nous : utiliser **l'interpréteur** de commande Python en tapant simplement la commande `python` dans la console et écrire ensuite les instructions les unes après les autres. Sinon, il faudra écrire une suite d'instructions dans un seul et même **fichier** Python. Nous passerons ensuite à l'interpréteur Python le fichier en **paramètre**. L'interpréteur se chargera de lire les instructions de haut en bas et de les exécuter les unes après les autres.

## Commenter le code

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
formateur = True
age = 30
prenom = "Jules"
```

### Les booléens

Le type de données élémentaire à connaître qui est à la base de l'informatique d'aujourd'hui est le booléen. Il s'agit d'un type de données qui n'a que deux valeurs possibles : `True`ou `False`. Cela correspond au `0` et au `1` du binaire. Nous l'utiliserons beaucoup lorsque nous aborderons les conditions.

```python
# Une vérité
je_suis_jeune = True

# Un mensonge
j_ai_des_enfants = False
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

Afin de stocker du texte (un prénom, un nom, une phrase, ...) nous utiliserons les `str` qui représentent les chaînes de caractères. Il y a deux méthodes pour déclarer un `str` (avec guillemets simples ou doubles):

```python
prenom = "Jules"
nom = 'Jules'
```

Parfois on peut avoir envie d'utiliser des **guillemets** dans la chaîne de caractères. Dans ce cas on peut procéder comme suit :

```python
presentation = "Je m'appelle Jules"
citation = '"Bienvue à Simplon!" - Jonathan.'
```

Parfois on peut avoir envie de combiner les deux :

```python
citation = '"Je suis le pape et j\'attends ma soeur" - Odile de Ray.'
```

Dans cette dernière citation, j'ai besoin **d'échapper** le guillemet simple afin qu'il ne soit pas interprété comme la fin de la chaîne de caractères. On utilise dans ce cas le caractère `backslash`.

On peut aussi avoir besoin d'écrire une chaine de caractères qui contient plusieurs lignes de texte. Dans ce cas, deux solutions : utiliser le caractère spécial `\n` pour indiquer un retour à la ligne ou utiliser le commentaire multiligne.

```python
presentation = "Je m'appelle Jules\nJ'ai 30 ans."
passions = """- Aviron
- Self-Hacking
- The Lord of the Ring"""
```

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/introduction.html#strings)

## Opérateurs

### Opérations de base sur des nombres

On peut utiliser les 4 opérations sur des nombres. Les résultats obtenus sont sans surprise.

```python
soldeCompte = 150
retrait = 20

nouveauSolde = soldeCompte - retrait

depot = 105
nouveauSolde = soldeCompte + depot
```

Les opérations **+,-,*** sur des nombres entiers donnent des nombres entiers.
Les opérations **+,-,*** sur au moins un nombre float donnent des nombres float.

```python
soldeCompte = 150
depot = 10.0

nouveauSolde = soldeCompte + depot

pourcentage = 0.3
nouveauSolde = soldeCompte * 0.3
```

La division a toujours pour résultat un float.

```python
nbPartPizza = 4
nbPersonne = 2

nbPart = 4/2 # 2.0
```

Les priorités de calcul sont les priorités habituelles, on peut utiliser des parenthèses.
```python
a = (2+4)*3 # 18
b = 2+4*3 # ?
```

### Puissance

L'opérateur puissance se note **

```python
a = 3 ** 2
```

### Division entière

On utilise souvent en informatique la division entière qui donne deux résultats : le reste et le quotient.

```python
etudiants = 26
nbGroupes = 3

etudiantsParGroupe = 26 // 3 # pour obtenir un résultat entier
etudiantsRestant = 26 % 3 # on dit 26 modulo 3
```

### Opérations avec des chaînes

On peut concaténer (mettre bout à bout) des chaînes de caractères avec l'opérateur +.

```python
nom = "Odile"
age = 34

presentation = "Bonjour, je m'appelle "+nom+ " et j'ai "+age+ " ans" # ne fonctionne pas, il faut convertir d'abord age en chaîne
presentation2 = "Bonjour, je m'appelle "+nom+ " et j'ai "+str(age)+ " ans"
```

On peut aussi utiliser d'autres opérations arithmétiques avec du texte.

```python
initial = "pain"
magic = 3*initial
```
### Comparaison

Les relations d'ordre produisent des booleans. Ils se basent sur l'ordre lexicographique (du dictionnaire).

```python
18 < 22 # True
3*5 < 10 # False
2*3 <= 6 # True
"la ligne rouge" < "apocalypse now" # False
"rocky3" > 2 # erreur
```

### Egalité

On compare des variables avec **==**, puisque le **=** est déjà utilisé pour l'affectation. Cela produit aussi un boolean.

```python
line1 = "Nah nah nah nah nah nah nah nah nah yeah";
line2 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";
line3 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";

line1 == line2
line2 == line3

isDifferent = line1 != line3 # il est vrai que ces lignes ne sont pas égales!
```


## Booleans et conditions

### Conditions

Pour effectuer un bloc d'instructions si une condition est vraie, on utilise le mot-clé **if**. Pour délimiter la taille du bloc d'instructions, on utilise l'indentation.

```python
temperature = 10
vetement = "teeshirt"

if temperature < 15 : # début du bloc après les :
  print("c'est deja l'automne")
  vetement = "pull"

print(vetement)

```
Si la condition est vraie, on exécute les instructions du blocs. Sinon on saute le bloc.
On peut ajouter un bloc à exécuter seulement si la condition est fausse avec **else**.

```python
temperature = 10
vetement = "teeshirt"

if temperature < 15 : # début du bloc après les :
  print("c'est deja l'automne")
  vetement = "pull"

else :
  print("vive le rechauffement")
  # pas la peine de changer de vetement

print(vetement)

```

On peut aussi ajouter d'autres conditions intermédiaires avec **elif**, a exécuter seulement si les précédentes sont fausses.


```python
age = 2

if age < 0 :
  print("merci d'entrer un age valide (positif)")

elif age < 3 : # on ne rentre pas ici si on est déjà entré dans le cas d'avant
  print("tarif : gratuit")

elif age < 18 :
  print("tarif : réduit")

elif age > 65 :
  print("tarif : réduit")

else : # dans tous les autres cas
  print("tarif : normal")
```

### Opérations sur les booleans

Dans le cas précédent, on obtient un tarif réduit si l'âge est inférieur à 18 **ou** supérieur à 65. On peut rassembler les deux cas.


```python
age = 2

if age < 0 :
  print("merci d'entrer un age valide (positif)")

elif age < 3 : # on ne rentre pas ici si on est déjà entré dans le cas d'avant
  print("tarif : gratuit")

elif age < 18 or age > 65 :
  print("tarif : réduit")

else : # dans tous les autres cas
  print("tarif : normal")
```

Une erreur classique est d'utiliser un **or** lorsqu'il faudrait un **and** ou inversement. Ici par exemple, un age qui est inférieur à 18 **et** supérieur à 65 n'existe pas, il fallait bien utiliser **ou**.

```
brocoli = 4
aubergine = 6
concombre = 5
radis = 2
pomme = 3
mure = 9
```
> quelle condition sur les prix pour ne sélectionner que :
```
brocoli = 4
radis = 2
pomme = 3
mure = 9
```
question tirée du concours [castor informatique](http://concours.castor-informatique.fr)

## Les fonctions

### Pourquoi utiliser des fonctions

Une fonction est un **bout de code** que l'on va définir afin d'être **réutilisé**. Pourquoi devrions-nous faire cela ? En programmation, nous cherchons à résoudre des problèmes, et comme nous l'avons vu en découvrant l'algorithmique très souvent nous pouvons **découper** un problème en plusieurs **sous-problèmes** à résoudre et cela nous aide à rendre le problème plus simple à résoudre. Une des premières utilité d'une fonction est donc de rendre le problème plus simple a résoudre en le découpant en sous problèmes. Cela a aussi l'avantage de rendre le code plus lisible en le découpant et en nommant les actions.

Si l'on se rappelle les notions d'algorithmique on a le programme suivant pour résoudre le problème de la cuisson des pâtes.

```
début
  remplir_casserole(eau)
  tant_que (eau_non_bouillante)
    chauffer_casserole(feu_max)
  fin_tant_que

  remplir_casserole(pâtes)
  tant_que (pâtes_non_cuites)
    chauffer_casserole(feu_vif)
  fin_tant_que

  égouter_pâtes
  servir_pâtes
fin
```

Chaque ligne de code peut être une fonction qu'il faut redécouper en actions plus précises. Par exemple `chauffer_casserole(feu_vif)` peut avoir plusieurs actions à réaliser comme `ouvrir_robinet_gaz(70%)`, `craquer_allumette()`, `approcher_allumette()` et `poser_casserole()`. En utilisant `chauffer_casserole(feu_vif)` dans notre programme global on comprend directement ce qu'il y a lieu de faire. Grâce à cette fonction `chauffer_casserole(feu_vif)` on gagne en lisibilité.

En plus cette fonction peut être réutilisée à différents endroits en fonction des besoins et avec différents **arguments**. Ici pour faire bouillir l'eau, on l'utilise avec l'argument `feu_max` puis pour cuire les pâtes avec l'argument `feu_vif`. Si on voulait faire cuire une ratatouille, on pourrait l'utiliser avec l'argument `feu_doux`.

### Définir et appeler des fonctions en Python

En Python, pour déclarer une fonction on procède de la manière suivante :

```python
def definir_prenom():
  prenom = "Jules"
```

Cette fonction ne fait pas grand chose, elle déclare juste une variable `prenom` à l'intérieur de la fonction qui contiendra la chaîne de caractères _Jules_. On peut maintenant **l'appeler** dans la suite de notre programme.

```python
def definir_prenom():
  prenom = "Jules"

definir_prenom()
```

Il ne se passera rien de bien intéressant mais nous avons défini notre première fonction !

Les fonctions deviennent **intéressantes** lorsque l'on :

- Définit des **paramètres**
- Renvoie une **valeur de retour**

```python
def dire_bonjour(prenom):
  return "Bonjour " + prenom

# Ici on range le retour de la fonction "Bonjour Jules" dans la variable message_bienvenue
message_bienvenue = dire_bonjour("Jules")
```

Avec cette fonction, je peux maintenant générer des messages de bienvenue différents car `dire_bonjour(prenom)` prend en **paramètre** une chaîne de caractères nommée `prenom` et **retourne** la valeur "Bienvenue _valeur de prenom_"

On peut définir autant d'arguments que l'on veut (même si ça va vite devenir compliqué si une fonction dépasse 5 arguments) et on ne pourra retourner qu'une seule valeur de retour.

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)

## listes

Il est souvent pratique de gérer plusieurs variables à l'aide de listes (ou de tableaux).

```python
eleve1 = "sam"
eleve2 = "bob"
eleve3 = "al"
# etc ...
```

Les éléments sont entre crochets et séparés par des virgules.

```python
eleves = ["sam", "bob", "al"]
# une seule variable !
```

On peut faire des listes de nombres, de chaînes, de booléens, etc ...

```python
listeNb = [1,2,3]
listeMot = ['celeri', 'muscade', 'agneau']
listeMixe = ['odile', 2, 'ray']

listeNb.reverse() # fonction de base
listeMot.sort() # trie en place
len(listeMot) # taille de la liste
```

### Indices

Les éléments sont numérotés à partir de 0. On accède aux éléments avec **[]**

```python
eleves = ["sam", "bob", "al", "odile"]
print(eleves[1]) # l'élément n°1 de la liste est bob
```

On peut extraire une sous-liste avec **:**

```python
eleves = ["sam", "bob", "al", "odile"]
print(eleves[1:3]) # les éléments 1 à 3 (exclu)
print(eleves[1:]) # tous les éléments à partir du 1
```

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/introduction.html#lists)


### Range

Python sait aussi compter! pour générer une liste de nombre, on utilise simplement la fonction **range**

```python
liste = range(2,10) # de 2 jusqu'à 10 (exclu)
liste2 = range(50) # de 0 jusqu'à 50 (exclu)
liste3 = range(1,50,2)
```

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/controlflow.html#the-range-function)

## Boucles

On va parler ici de répétitions. C'est quelque chose qu'un programme sait très bien faire, répéter plusieurs fois (parfois un grand nombre) un bloc d'instructions.

### While (tant que)

Tant que tu n'auras pas fini ta purée, tu n'auras pas de dessert!

```python
puree = 10 # cuilleres

while puree > 0 : # puree > 0 est une condition, comme pour le if
  print("une cuillère pour papa")
  puree = puree -1

dessert = "fondant au chocolat"
```

### For (pour)

Si on veut faire le même traitement pour chaque élément d'une liste, il suffit d'utiliser le mot **pour**, mais en anglais. Dans ce cas, on doit choisir un nom pour l'élément courant à parcourir.

```python
eleveListe = ["sam", "bob", "al", "odile"]

for eleve in eleveListe : # on commence toujours un bloc avec :
  print("bonjour "+eleve)

```

Ou aussi avec des nombres, pour répéter 100 fois une action (utile!).

```python
for i in range(100) :
  print(str(i)+" Je ne photocopierai plus mes fesses")
```

[ref](https://fr.wikipedia.org/wiki/Liste_des_phrases_au_tableau_noir_des_Simpson)

Pour plus de détails : [La documentation officielle de Python](https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements)


## Entrées / Sorties

Lorsque l'on exécute un programme, on peut avoir besoin de lui fournir des données en entrée ou bien d'en récupérer en sortie. Plusieurs méthodes existent et nous allons en explorer deux : en utilisant la **console** et les **fichiers**.

### Console

La console (ou terminal) est une interface en ligne de commande qui permet de dialoguer avec notre machine en lui écrivant des **instructions** et en lisant les **retours** faits une fois les instructions réalisées. Lorsque nous écrivons un programme Python dans un fichier et que nous lançons ce programme via la console, les instructions du programme s'enchaîne et on reprend la main sur la console lorsque toutes les instructions du programme sont terminées. On pourrait avoir envie d'afficher des informations lors de la réalisation du programme et aussi de demander à l'utilisateur d'en saisir.

Pour **afficher** quelque chose dans la console, il suffit d'utiliser l'instruction `print()`.

Pour **récupérer une entrée utilisateur**, il suffit d'utiliser la fonction `input()`.

```python
def dire_bonjour(prenom):
    return "Bonjour " + prenom

prenom_utilisateur = input("Bonjour, comment t'appelles-tu ? ")

print(dire_bonjour(prenom_utilisateur))
```

### Fichiers

Parfois nous aurons aussi besoin de lire ou d'écrire dans des fichiers. Dans les deux cas, il faudra ouvrir le fichier et lire ou écrire dedans.

Pour ouvrir un fichier il faut utiliser la fonction `open()` et lui donnant en argument l'emplacement du fichier et le mode (façon dont on va utiliser le fichier). Pour le mode, on peut utiliser `'r'` pour lire, `'w'` pour écrire, '`a`' pour écrire à la fin ou '`r+`' pour lire et écrire.

#### Lire

Ci dessous un exemple de lecture de la première ligne d'un fichier markdown. On utilisera la fonction `readline()` pour récupérer le contenu d'une ligne du fichier que nous souhaitons lire.

```python
f = open('convention.md', 'r')
print(f.readline())
f.close()
```

Si l'on veut lire toutes les lignes du fichier on peut écrire le code suivant :

```python
f = open('convention.md', 'r')

for line in f:
    print(line)

f.close()
```

Dans cet exemple, il est important de noter que l'on ouvre le fichier avant de lire ses lignes et une fois la lecture terminée, on le ferme avec la fonction `close()`. On peut simplifier ce fonctionnement grâce à l'instruction `with` qui fermera automatiquement le fichier pour nous :

```python
with open('convention.md', 'r') as f:
    for line in f:
        print(line)

print('end')
```

#### Ecrire

Ci dessous un exemple d'écriture d'une ligne dans fichier texte. On utilisera la fonction `write()` pour écrire du contenu dans un fichier.

```python
f = open('./session1/exercice/output.data', 'w')
f.write('Mon premier fichier écrit en Python')
f.close()
```
