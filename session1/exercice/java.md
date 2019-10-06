- [Étape 1 : Déclarons quelques variables](#orged68558)
- [Étape 2 : Utilisons des opérateurs](#orgdd6745c)
  - [Calcul de prix TTC](#org4ce3bd4)
  - [Calcul composé](#org3844edb)
- [Étape 3 : Algorithmes](#org02d27cb)
  - [Compréhension de code](#orgc26c613)
  - [Factorielles](#orgbb44a39)
  - [Affichage](#org8478473)
    - [1D](#orgfd77c5f)
    - [2D](#org6e4fc70)
  - [Chaîne de caractères](#orgeac5313)
  - [Nombres premiers](#org17d40bf)
  - [Tables](#orgdd846c3)
  - [Représentation de table](#orgd39e54d)
    - [Table vide](#org09ee162)
    - [Table remplie](#org0aba34a)



<a id="orged68558"></a>

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


<a id="orgdd6745c"></a>

# Étape 2 : Utilisons des opérateurs


<a id="org4ce3bd4"></a>

## Calcul de prix TTC

Déclarer une variable `prixHT` et une variable `tauxTVA`. Calculer et mettre dans une variable le prix TTC.


<a id="org3844edb"></a>

## Calcul composé

Soit une variable `year`. Calculer et mettre dans une variable si cette année est bissextile ou non.


<a id="org02d27cb"></a>

# Étape 3 : Algorithmes


<a id="orgc26c613"></a>

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


<a id="orgbb44a39"></a>

## Factorielles

Écrire un programme qui affiche la factorielle d'un nombre.


<a id="org8478473"></a>

## Affichage


<a id="orgfd77c5f"></a>

### 1D

Écrire un programme qui affiche une règle graduée d'une longueur `n`, avec des graduations tous les 5 pas. Par exemple :

-   **n = 1:** `[-]`
-   **n = 6:** `[----+-]`
-   **n = 10:** `[----+----]`
-   **n = 12:** `[----+----+--]`


<a id="org6e4fc70"></a>

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


<a id="orgeac5313"></a>

## Chaîne de caractères

Écrire un programme qui affiche si une chaîne de caractères donnée est un palindrome ou non.


<a id="org17d40bf"></a>

## Nombres premiers

-   Écrire un programme qui permette de savoir si un nombre donné est premier ou non.
-   Écrire un programme qui affiche les nombres premiers inférieurs ou égaux à un nombre donné.


<a id="orgdd846c3"></a>

## Tables

Écrire un programme qui permette d'afficher la table de multiplication jusqu'à n × m. Par exemple :

-   **n = 3, m = 4:** 

```org
 1  2  3  4
 2  4  6  8
 3  6  9 12
```


<a id="orgd39e54d"></a>

## Représentation de table


<a id="org09ee162"></a>

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


<a id="org0aba34a"></a>

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
