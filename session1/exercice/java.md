- [Étape 1 : Déclarons quelques variables](#orgbbc466a)
- [Étape 2 : Utilisons des opérateurs](#org092f5b7)
  - [Calcul de prix TTC](#org39f13f1)
  - [Calcul composé](#orgad2b878)
- [Étape 3 : Algorithmes](#orgf98c7e2)
  - [Compréhension de code](#org9f92fcd)
  - [Factorielles](#org465ad8a)
  - [Affichage](#orge04ce4c)
    - [1D](#org3f8ac11)
    - [2D](#orgc78eab4)
  - [Chaîne de caractères](#orgd4becc6)
  - [Nombres premiers](#orgb42f820)
  - [Tables](#org6366e33)
  - [Représentation de table](#orged190c3)
    - [Table vide](#orgf613c96)
    - [Table remplie](#orgf4032f1)
- [Étape 4 : Entrées / Sorties](#org6b8e1fd)
  - [Console](#orgf917617)
    - [Saisies au clavier](#org8f2b98a)
    - [Menu](#orgb00659e)
  - [Fichier](#orgbc0f493)
  - [Gestion d'erreur](#org9f111c8)
    - [Saisie de nombre](#org0114f54)
    - [Problème d'accès fichier](#org1e8ab2a)



<a id="orgbbc466a"></a>

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


<a id="org092f5b7"></a>

# Étape 2 : Utilisons des opérateurs


<a id="org39f13f1"></a>

## Calcul de prix TTC

Déclarer une variable `prixHT` et une variable `tauxTVA`. Calculer et mettre dans une variable le prix TTC.


<a id="orgad2b878"></a>

## Calcul composé

Soit une variable `year`. Calculer et mettre dans une variable si cette année est bissextile ou non.


<a id="orgf98c7e2"></a>

# Étape 3 : Algorithmes


<a id="org9f92fcd"></a>

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


<a id="org465ad8a"></a>

## Factorielles

Écrire un programme qui affiche la factorielle d'un nombre.


<a id="orge04ce4c"></a>

## Affichage


<a id="org3f8ac11"></a>

### 1D

Écrire un programme qui affiche une règle graduée d'une longueur `n`, avec des graduations tous les 5 pas. Par exemple :

-   **n = 1:** `[-]`
-   **n = 6:** `[----+-]`
-   **n = 10:** `[----+----]`
-   **n = 12:** `[----+----+--]`


<a id="orgc78eab4"></a>

### 2D

Écrire un programme qui affiche un rectangle de taille `nColonnes` par `nLignes`. Par exemple :

-   **nColonnes = 1, nLignes = 1:** 

```org
+-+
| |
+-+
```

-   **nColonnes = 2, nLignes = 1:** 

```org
+---+
|   |
+---+
```

-   **nColonnes = 3, nLignes = 2:** 

```org
+-----+
|     |
|     |
|     |
+-----+
```


<a id="orgd4becc6"></a>

## Chaîne de caractères

Écrire un programme qui affiche si une chaîne de caractères donnée est un palindrome ou non.


<a id="orgb42f820"></a>

## Nombres premiers

-   Écrire un programme qui permette de savoir si un nombre donné est premier ou non.
-   Écrire un programme qui affiche les nombres premiers inférieurs ou égaux à un nombre donné.


<a id="org6366e33"></a>

## Tables

Écrire un programme qui permette d'afficher la table de multiplication jusqu'à n × m. Par exemple :

-   **n = 3, m = 4:** 

```org
 1  2  3  4
 2  4  6  8
 3  6  9 12
```


<a id="orged190c3"></a>

## Représentation de table


<a id="orgf613c96"></a>

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


<a id="orgf4032f1"></a>

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


<a id="org6b8e1fd"></a>

# Étape 4 : Entrées / Sorties


<a id="orgf917617"></a>

## Console


<a id="org8f2b98a"></a>

### Saisies au clavier

Modifier le code déjà écrit pour lire les données au clavier.


<a id="orgb00659e"></a>

### Menu

Écrire un programme qui propose d'exécuter les différentes fonctionnalités implémentées en choisissant à partir d'un menu.


<a id="orgbc0f493"></a>

## Fichier

Modifier le programme précédent pour qu'il puisse prendre en compte un argument au lancement du programme. Si le programme reçoit un argument, il doit être utilisé comme le nom d'un fichier dans lequel chercher toutes les données (y compris les choix de menus).


<a id="org9f111c8"></a>

## Gestion d'erreur


<a id="org0114f54"></a>

### Saisie de nombre

Modifier le programme précédent pour que, si une saisie invalide est faite dans le menu, une nouvelle saisie soit proposée.


<a id="org1e8ab2a"></a>

### Problème d'accès fichier

Modifier le programme précédent pour que, si un nom de fichier est passé en argument mais que l'accès à celui-ci n'est pas possible, un nouveau nom de fichier soit demandé interactivement.
