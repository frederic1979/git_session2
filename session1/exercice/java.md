- [Étape 1 : Déclarons quelques variables](#org87d68d2)
- [Étape 2 : Utilisons des opérateurs](#orge0ee033)
  - [Calcul de prix TTC](#orgf2a2ca2)
  - [Calcul composé](#org2a493e2)
- [Étape 3 : Algorithmes](#org4a38c2c)
  - [Compréhension de code](#org5e4c48e)
  - [Factorielles](#org5fd2cb8)
  - [Affichage](#org231f826)
    - [1D](#orgafe126f)
    - [2D](#org888fd8b)
  - [Chaîne de caractères](#orgec505d4)
  - [Nombres premiers](#orgccb5a43)
  - [Tableaux](#org6fec945)
    - [1D](#orgb84dfd1)
    - [2D](#org6140c32)
  - [Tables](#orga618ec1)
  - [Représentation de table](#org0ef272f)
    - [Table vide](#org09b8bb3)
    - [Table remplie](#orgcd4dc30)
- [Étape 4 : Entrées / Sorties](#org995545f)
  - [Console](#orga8bdf4a)
    - [Saisies au clavier](#org0c84f42)
    - [Menu](#orgbfbd810)
  - [Fichier](#orgbc1f60b)
  - [Gestion d'erreur](#orgf40a113)
    - [Saisie de nombre](#org76d253e)
    - [Problème d'accès fichier](#orgef2b83e)



<a id="org87d68d2"></a>

# Étape 1 : Déclarons quelques variables

Dans un premier temps, on va juste déclarer quelques variables locales dans une fonction `main` d'une classe `ExosIntro` d'un projet `Exos`.

-   **À faire:** déclarer des variables permettant de vous décrire avec :
    -   Votre prénom
    -   Votre nom
    -   Votre âge
    -   Votre taille en cm
    -   Quelques lignes qui expliquent pourquoi vous rejoignez la formation
    -   Le montant d'un compte bancaire
    -   Le fait qu'une année soit bissextile ou non
    -   La *couleur* d'une carte de jeu de cartes
    -   Une couleur ‽


<a id="orge0ee033"></a>

# Étape 2 : Utilisons des opérateurs


<a id="orgf2a2ca2"></a>

## Calcul de prix TTC

Déclarer une variable `prixHT` et une variable `tauxTVA`. Calculer et mettre dans une variable le prix TTC.


<a id="org2a493e2"></a>

## Calcul composé

Soit une variable `year`. Calculer et mettre dans une variable si cette année est bissextile ou non.


<a id="org4a38c2c"></a>

# Étape 3 : Algorithmes


<a id="org5e4c48e"></a>

## Compréhension de code

Essayer de deviner / comprendre ce que fait le code suivant :

```java
public class Mystere{
    public static void main(String[] args){
	System.out.println(mystere(0.01f));
    }
    public static float mystere(float epsilon){
	return mystere(0.f, Float.MAX_VALUE, epsilon);
    }
    public static float mystere(float min, float max, float epsilon){
	while((max != min)){
	    float m = max/2 + min/2;
	    if((m + epsilon) > m){
		min = Math.nextUp(m);
	    }else{
		max = m;
	    }
	}
	return min;
    }
}
```


<a id="org5fd2cb8"></a>

## Factorielles

Écrire un programme qui affiche la factorielle d'un nombre.


<a id="org231f826"></a>

## Affichage


<a id="orgafe126f"></a>

### 1D

Écrire un programme qui affiche une règle graduée d'une longueur `n`, avec des graduations tous les 5 pas. Par exemple :

-   **n = 1:** `[-]`
-   **n = 6:** `[----+-]`
-   **n = 10:** `[----+----+]`
-   **n = 12:** `[----+----+--]`


<a id="org888fd8b"></a>

### 2D

Écrire un programme qui affiche un rectangle de taille `nColonnes` par `nLignes`. Par exemple :

-   **nColonnes = 1, nLignes = 1:** 

```org
+-+
| |
+-+
```

-   **nColonnes = 3, nLignes = 1:** 

```org
+---+
|   |
+---+
```

-   **nColonnes = 5, nLignes = 3:** 

```org
+-----+
|     |
|     |
|     |
+-----+
```


<a id="orgec505d4"></a>

## Chaîne de caractères

Écrire un programme qui affiche si une chaîne de caractères donnée est un palindrome ou non.


<a id="orgccb5a43"></a>

## Nombres premiers

-   Écrire un programme qui permette de savoir si un nombre donné est premier ou non.
-   Écrire un programme qui affiche les nombres premiers inférieurs ou égaux à un nombre donné.


<a id="org6fec945"></a>

## Tableaux


<a id="orgb84dfd1"></a>

### 1D

-   **Nombres:** Écrire un programme qui permette d'afficher la valeur maximale d'un tableau de nombres.
-   **Chaînes de caractères:** Écrire un programme qui permette d'afficher la taille de la chaîne de caractères la plus longue d'un tableau de chaînes de caractères.


<a id="org6140c32"></a>

### 2D

-   **Nombres:** Écrire un programme qui permette d'afficher la valeur maximale d'un tableau de tableaux de nombres.
-   **Chaînes de caractères:** Écrire un programme qui permette d'afficher la taille de la chaîne de caractères la plus longue d'un tableau de tableaux de chaînes de caractères.


<a id="orga618ec1"></a>

## Tables

Écrire un programme qui permette d'afficher la table de multiplication jusqu'à n × m. Par exemple :

-   **n = 3, m = 4:** 

```org
 1  2  3  4
 2  4  6  8
 3  6  9 12
```


<a id="org0ef272f"></a>

## Représentation de table


<a id="org09b8bb3"></a>

### Table vide

Écrire un programme qui permet d'afficher une table, en représentant les lignes et les colonnes, de `nColonnes` par `nLignes`. Par exemple :

-   **nColonnes = 1, nLignes = 1:** 

```org
┏━┓
┃ ┃
┗━┛
```

-   **nColonnes = 2, nLignes = 1:** 

```org
┏━┳━┓
┃ ┃ ┃
┗━┻━┛
```

-   **nColonnes = 3, nLignes = 2:** 

```org
┏━┳━┳━┓
┃ ┃ ┃ ┃
┣━╋━╋━┫
┃ ┃ ┃ ┃
┗━┻━┻━┛
```


<a id="orgcd4dc30"></a>

### Table remplie

Écrire un programme qui permette d'afficher une table de multiplication jusqu'à n × m en représentant les lignes et les colonnes. Par exemple :

-   **n = 2, m = 3:** 

```org
┏━┳━┳━┓
┃1┃2┃3┃
┣━╋━╋━┫
┃2┃4┃6┃
┗━┻━┻━┛
```

-   **n = 3, m = 4:** 

```org
┏━━┳━━┳━━┳━━┓
┃ 1┃ 2┃ 3┃ 4┃
┣━━╋━━╋━━╋━━┫
┃ 2┃ 4┃ 6┃ 8┃
┣━━╋━━╋━━╋━━┫
┃ 3┃ 6┃ 9┃12┃
┗━━┻━━┻━━┻━━┛
```


<a id="org995545f"></a>

# Étape 4 : Entrées / Sorties


<a id="orga8bdf4a"></a>

## Console


<a id="org0c84f42"></a>

### Saisies au clavier

Modifier le code déjà écrit pour lire les données au clavier.


<a id="orgbfbd810"></a>

### Menu

Écrire un programme qui propose d'exécuter les différentes fonctionnalités implémentées en choisissant à partir d'un menu.


<a id="orgbc1f60b"></a>

## Fichier

Modifier le programme précédent pour qu'il puisse prendre en compte un argument au lancement du programme. Si le programme reçoit un argument, il doit être utilisé comme le nom d'un fichier dans lequel chercher toutes les données (y compris les choix de menus).


<a id="orgf40a113"></a>

## Gestion d'erreur


<a id="org76d253e"></a>

### Saisie de nombre

Modifier le programme précédent pour que, si une saisie invalide est faite dans le menu, une nouvelle saisie soit proposée.


<a id="orgef2b83e"></a>

### Problème d'accès fichier

Modifier le programme précédent pour que, si un nom de fichier est passé en argument mais que l'accès à celui-ci n'est pas possible, un nouveau nom de fichier soit demandé interactivement.
