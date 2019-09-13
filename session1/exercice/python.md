# Exercices Python

## Etape 1 : Déclarons quelques variables

Dans un premier temps nous allons simplement utiliser l'interpréteur Python. Pour cela il suffit d'ouvrir un terminal et de taper la commande `python`. Vous devriez voir dans votre terminal en début de ligne `>>>`. Si c'est le cas, c'est le signe que vous pouvez écrire du Python.

A faire : déclarer des variables permettant de vous décrire avec :

- Votre prénom
- Votre nom
- Votre age
- Votre taille en cm
- Quelques lignes qui expliquent pourquoi vous rejoignez la formation

## Etape 2 : Utilisons les opérateurs

### Ex1
```python
mystery1 = 8 + 6
mystery2 = 8 - 6
```
Afficher avec **print** la variable qui est égale à -2.

### Ex2
```python
zebrasInZoo = 8
giraffesInZoo = 4
```
Créer une variable **animalsInZoo** qui contient le nombre total d'animaux dans le zoo. Afficher cette variable.

### Ex3
```python
prixInitial = 1500
tva = 0.20
```
Créer une variable **prixFinal** qui égale au prix initial plus le prix initial multiplié par la tva. Afficher cette variable.

### Ex4 : modulo et division entière
1. Remplir des boites de 6 oeufs! Créer une variable **nbBoites** qui contient le nombre de boites pleines et une variable **nbOeufsRestant** pour le nombre d’œufs qui restent.

```python
nbOeufsParBoite = 6
nbOeufsTotal = 145

nbBoites
```

2. Dans un jeu de 32 cartes (7,8,9,.., roi, as pour pique, cœur, carreau, trèfle), on décide d'associer à chaque carte un numéro.
Le numéro de la carte est obtenu en multipliant le numéro de la couleur (1,2,3 ou 4) par le numéro de la figure (1,2,3 ... 8).

Exemple :
le 9 de pique a pour numéro = 3*1 = 3 (3e carte de la couleur 1)
la dame de cœur a pour numéro = 6*2 = 12

```python
numeroCarteMystere = 28
```
Créer une variable **numeroCouleur** et **numeroFigure** à retrouver à partir du numéro de la carte mystère. Vous pouvez vérifier que votre méthode fonctionne en retrouvant la couleur de la carte n°3 (9 de pique) ou de la carte n°12 (dame de cœur).

### Ex5 : inférieur, supérieur
```python
prixInitial = 1500
tva = 0.20

budget = 2000
```
Créer une variable **budgetSuffisant** qui indique si le budget est supérieur ou égal au prix initial plus le prix initial multiplié par la tva. Afficher cette variable.

### Ex6 : égalité
Pour éviter les doublons, on cherche à comparer des albums par rapport à leur durée totale et au nombre de chansons par album.

```python
songsA = 9
songsB = 9
albumLengthA = 41
albumLengthB = 53
```
Créer une variable **sameSongs** qui est vraie si les deux albums contiennent le même nombre de chansons.
Créer une variable **sameAlbumLength** qui est vraie si les deux albums ont la même longueur au total. Afficher ces variables.

### Ex7 : chaînes et nombres

```python
formateur = 'Jules'
langage = 'java'
version = 1.8
```

Créer une variable **description** du type :
Mon formateur <formateur> est fan de <langage>, surtout depuis la version <version>!!

Et afficher cette variable.

## Etape 3 : Conditionnons notre code

@Joss'

## Etape 4 : Créons des fonctions

- Créer une fonction qui renvoit l'aire d'un triangle en prenant en paramètres base et hauteur.
- Créer une fonction qui renvoit le volume d'une sphère en prenant en paramètre son rayon.
- Créer une fonction qui renvoit un message donnant l'IMC d'une personne. Elle prendra en paramètre le prénom de la personne, son poids en kg et sa taille en cm.

## Etape 5 : Tableaux

@Joss'

## Etape 6 : Boucles

@Joss'

## Etape 7 : Entrées / Sorties

<<<<<<< HEAD
- Créer un programme qui demande à l'utilisateur de se présenter : prénom, nom et age. Utilisez la console pour afficher un message d'accueil personnalisé du type "Bonjour _Jules Grand_ tu as _30 ans_ c'est bien ça ?"
- Créer un programme qui fera la même chose tout en écrivant les informations reçues dans un fichier texte. Le fichier devra être nommé _prenom-nom.txt_
- Créer un programme qui va lire le fichier [films-2018.txt](../resource/films-2018.txt) et indiquer combien il y a de films sortis en 2018.

**Bonus**

- Créer un programme qui va lire le fichier [villes-france.txt](../resource/villes-france.txt) et indiquer combien de fois apparaît _TOULOUSE_ dans le fichier.
- Créer un programme qui va lire le fichier [villes-france.txt](../resource/villes-france.txt) et créer un nouveau fichier sans doublons (après modification, le nouveau fichier ne doit contenir qu'une seule fois le même nom de ville).
- Créer un programme qui va lire le fichier [villes-france.txt](../resource/villes-france.txt) et créer un nouveau fichier dans lequel chaque ligne donnera le nom d'une ville en affichant le nombre d'occurence dans le fichier de départ. Ce fichier devra être trié par ordre alphabétique.
=======
@Jules
>>>>>>> 3ffee1f1e292dbadd62b75aa26e6debbbc0564f3
