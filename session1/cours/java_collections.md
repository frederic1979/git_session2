- [Limites des tableaux](#org23034cb)
- [Introduction aux classes génériques](#org3661122)
  - [Pourquoi des classes génériques ?](#org83dd9ef)
  - [Les classes 'wrappers'](#org29a6baa)
- [Stocker un nombre indéterminé d'éléments](#orgbe4088b)
  - [Listes](#orgbb904ef)
  - [Piles (*Stack*)](#orgf4d160f)
  - [Files (*Queues*)](#org0d16045)
- [Stocker et rechercher des valeurs sans doublons](#org562f855)
- [Associer des valeurs à des clés](#orgcf43958)
- [Implémenter des classes qui peuvent être utilisées dans des Collections](#org0eca174)
  - [equals](#org2330e27)
  - [hashCode](#orgcf366b7)
  - [Interface Comparable ou objet Comparator](#org3268424)
- [Interfaces](#org9806d7f)
  - [List](#org21144ed)
  - [Set](#orgb31047d)
  - [Map](#orgc1efd1d)
  - [Collection](#orgb6cfcc6)
- [Webliographie](#org055a94e)



<a id="org23034cb"></a>

# Limites des tableaux

Si l'on peut tout faire avec les types primitifs et des tableaux comme "briques de base", certaines fonctionnalités nécessitent une implémentation non triviales pour être performantes.

-   **Exercice:** Proposer un algorithme, voire une implémentation, pour stocker un nombre indéterminé à priori d'éléments (par exemple les lignes d'un fichier). Que penser de son efficacité ?

La bibliothèque standard met à notre disposition, dans le *package* `java.util` des classes qui implémentent les principales *structures de données* qui permettent de gérer efficacement des principaux cas d'utilisations.


<a id="org3661122"></a>

# Introduction aux classes génériques

Les classes implémentant les structures de données sont différentes des classes comme `String` ou `Scanner`. En effet, elles sont *paramétrées* par un(ou plus) nom de classe. Par exemple : `ArrayList<String>`.

Il s'agit de [classes génériques](https://en.wikipedia.org/wiki/Generics_in_Java).


<a id="org83dd9ef"></a>

## Pourquoi des classes génériques ?

En fait, on pourrait stocker des objets de n'importe quel type (n'importe quelle classe) car tous les objets peuvent être considérés comme des instances de la classe [Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) <sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.

De telles structures de données permettraient d'avoir des collections *hétérogènes*, mais surtout ne permettraient pas d'assurer que des collections sont *homogènes*, ce qui est le cas le plus fréquent, perdant l'intérêt du typage statique. C'est en essayant d'utiliser une valeur récupérée dans une collection qu'on aurait une erreur à l'exécution, alors qu'on aurait voulu avoir une erreur de compilation à l'insertion puisque c'est là qu'était l'erreur.

```java
 1  import java.util.ArrayList;
 2  
 3  public class HeterogenousContainerError{
 4      static ArrayList data = new ArrayList();
 5  
 6      public static void main(String[] args){
 7  	try {
 8  	    createData(true);
 9  	    createData(true);
10  	    createData(false);
11  	    createData(true);
12  	    
13  	    useData();
14  	    useData();
15  	    useData();
16  	}catch(Exception e){
17  	    e.printStackTrace(System.out);
18  	}
19      }
20      public static void createData(boolean valid){
21  	data.add( valid ? 1 : "1");
22      }
23      public static int useData(){
24  	int res = ((Integer)data.get(data.size()-1))*2;
25  	data.remove(data.size()-1);
26  	return res;
27      }
28  }
```

java.lang.ClassCastException: java.lang.String cannot be cast to java.lang.Integer at HeterogenousContainerError.useData(HeterogenousContainerError.java:24) at HeterogenousContainerError.main(HeterogenousContainerError.java:14) java.lang.ClassCastException: java.lang.String cannot be cast to java.lang.Integer at HeterogenousContainerError.useData(HeterogenousContainerError.java:24) at HeterogenousContainerError.main(HeterogenousContainerError.java:14)


<a id="org29a6baa"></a>

## Les classes 'wrappers'

On vient de voir que les classes implémentant les structures de données permettent de stocker n'importe quel *objet*. Mais on peut vouloir stocker des valeurs de types primitifs. Pour chaque type primitif, Java met à disposition une [classe wrapper](https://en.wikipedia.org/wiki/Primitive_wrapper_class) qui permet, [entre autres](https://docs.oracle.com/javase/tutorial/java/data/numberclasses.html), de stocker la valeur de type primitif à l'intérieur d'un objet. Par exemple, on a vu la classe [Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html) (plus précisément `java.lang.Integer`) qui correspond au type primitf `int`.

-   **Exercice:** Trouver les classes correspondant aux autres types primitifs.

Ces classes permettent les conversions automatique depuis/vers les types primitifs ([autoboxing / unboxing](https://docs.oracle.com/javase/tutorial/java/data/autoboxing.html)), comme par exemple à la ligne 21 du [src-HeterogenousContainerError](#src-HeterogenousContainerError).

-   **Exercice:** Comprendre pourquoi il n'y a pas d'auto-unboxing à la ligne 24 .


<a id="orgbe4088b"></a>

# Stocker un nombre indéterminé d'éléments

Lorsqu'on veut stocker un nombre a priori indéterminé de valeurs, suivant qu'on s'intéresse à pouvoir efficacement :

-   ajouter des valeurs
-   ajouter et retirer des valeurs :
    -   En retirant d'abord la dernière valeur ajoutée
    -   En retirant d'abord la première valeur ajoutée

Ces trois cas d'utilisation correspondent à différentes classes de la bibliothèque standard.


<a id="orgbb904ef"></a>

## Listes

-   **[java.util.ArrayList<E>](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) (où E est la classe des éléments à stocker):** c'est la classe qui correspond aux listes de python. Elle permet d'ajouter efficacement des éléments en fin de liste avec [add](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html#add-E-) ou de supprimer efficacement le dernier élément en passant [.size()-1](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html#size--) en argument à [remove(int index)](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html#remove-int-). Elle permet aussi des accès *aléatoire* (*random access*) permettant d'accéder à n'importe quel élément en indiquant l'indice ([get(int index)](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html#get-int-)).
-   **[java.util.LinkedList<E>](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) (où E est la classe des éléments à stocker):** c'est une [liste doublement chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e#Liste_doublement_cha%C3%AEn%C3%A9e) qui permet donc des ajout, accès et suppressions efficaces en début ou en fin de liste avec, respectivement, [addFirst](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#addFirst-E-), [getFirst](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#getFirst--) et [removeFirst](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#removeFirst--) ou [addLast](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#addLast-E-), [getLast](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#getLast--) et [removeLast](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html#removeLast--). En revanche, elle ne permet pas d'accès efficace à n'importe quel élément : pour la traverser efficacement, il faut accéder aux éléments dans l'ordre.

-   **Exercice:** Utiliser une ArrayList pour lire les lignes d'un [fichier texte](file:///home/bernard/Documents/Workspaces/Teaching/corp-bnp-renault/session1/ressource/books/Spinoza/Spinoza-Ethique.txt).


<a id="orgf4d160f"></a>

## Piles (*Stack*)

Les structures de données de type *LIFO* (Last In First Out), ou *piles/(/Stack*<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>) (car comme sur une pile d'objet, on enlève le dernier élément ajouté), peuvent être réalisées efficacement avec une [java.util.ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) en ajoutant et retirant en fin de liste. Elles peuvent aussi être implémentées avec une [java.util.LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html), soit en ajoutant et retirant en début de liste, soit en ajoutant et retirant en fin de liste.


<a id="org0d16045"></a>

## Files (*Queues*)

Les structures de données de type *FIFO* (First In First Out), ou *files* (*Queue*), peuvent être implémentées par une [java.util.LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) en ajoutant en début de liste et retirant en fin de liste (ou l'inverse).


<a id="org562f855"></a>

# Stocker et rechercher des valeurs sans doublons

Si l'on veut stocker des valeurs sans doublons <sup><a id="fnr.3" class="footref" href="#fn.3">3</a></sup> et pouvoir tester efficacement si un certain *ensemble* contient déjà une valeur donnée, on peut utiliser l'un des classes suivantes :

-   **[HashSet<E>](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html):** c'est une structure de données qui stocke les éléments "dans le désordre" de façon à les indexer et pouvoir y accéder rapidement en fonction de leur valeur. Ainsi, la méthode [contains](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html#contains-java.lang.Object-) est très efficace.
-   **[TreeSet<E>](https://docs.oracle.com/javase/8/docs/api/java/util/TreeSet.html):** c'est une structure de données qui stocke les éléments selon un ordre, afin de pouvoir faire des recherche dichotomiques. Elle est en générale un peu moins performante que [HashSet<E>](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html) mais permet d'accéder aux éléments dans l'ordre.

-   **Exercice:** Permettre de recherche efficacement si des noms de domaine sont dans [une liste de noms de domaines *blacklistés*](file:///home/bernard/Documents/Workspaces/Teaching/corp-bnp-renault/session1/ressource/hosts/bad-hosts.txt).


<a id="orgcf43958"></a>

# Associer des valeurs à des clés

Les tableaux permettent d'associer une valeur (le contenu d'une case du tableau) à un indice compris entre 0 et `(nombre de cases du tableau - 1)`. On peut vouloir généraliser ce genre d'association à tous types de *clés*, par exemple pour pouvoir associer des adresses IP à des noms de domaines. C'est ce que permettent les *dictionnaires* en python où les tables d'association (*maps*) en Java. Elles sont paramétrées par deux types, le paramétrage `<K,V>` indiquant, respectivement, la classe de la clé et la classe de la valeur associée. On associe une valeur `v` de classe `V` à la clé `k` de type `K` avec la méthode [put(K k, V v)](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html#put-K-V-). On récupère la valeur associée à la clé `k` avec la méthode [get(K k)](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html#get-java.lang.Object-). Pour permettre de trouver efficacement la valeur associée à une clé, les clés des tables d'association sont organisées de façon similaire aux éléments d'un ensemble. On aura donc les deux classes suivantes, suivant que les clés soient indexées ou ordonnées :

-   **[HashMap<K,V>](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html):** c'est une table d'association dans laquelle les clés sont indexées pour permettre un accès très efficace.
-   **[TreeMap<K,V>](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html):** c'est une table d'association dans laquelle les clés sont ordonnées pour permettre un accès par recherche dichotomique.

-   **Exercice:** Compter le nombre d'occurrences de chaque mot dans [un fichier de mots](file:///home/bernard/Documents/Workspaces/Teaching/corp-bnp-renault/session1/ressource/books/mots.txt).


<a id="org0eca174"></a>

# Implémenter des classes qui peuvent être utilisées dans des Collections

On peut utiliser les structures de données pour stocker des instances de [String](https://docs.oracle.com/javase/9/docs/api/java/lang/String.html) et de toutes les classes *wrapper* de tous les types primitifs ([Integer](https://docs.oracle.com/javase/9/docs/api/java/lang/Integer.html), [Long](https://docs.oracle.com/javase/9/docs/api/java/lang/Long.html), [Float](https://docs.oracle.com/javase/9/docs/api/java/lang/Float.html), [Double](https://docs.oracle.com/javase/9/docs/api/java/lang/Double.html), …). Lorsqu'on voudra pouvoir stocker des instances de classes que nous définirons nous-mêmes (cf. /Programmation Orientée Objet), il faudra prendre de soin de définir correctement quelques méthodes pour que les instances de nos classes soient utilisables dans ces structures de données.


<a id="org2330e27"></a>

## equals

Même si elle n'est pas aussi performante que pour les ensembles (*sets*), les listes proposent aussi une méthode [contains](https://docs.oracle.com/javase/8/docs/api/java/util/List.html#contains-java.lang.Object-) qui permet de savoir si un élément est contenu dans la liste. Les tables d'association (*maps*) permettent efficacement, elles, de savoir si une clé est présente dans la table. Dans tous ces cas, il s'agit de trouver un élément (ou une clé) **égal** à l'argument et non pas seulement **identique**. Il faut donc que l'égalité soit définie, ce qui se fait en Java en redéfinissant la [méthode equals](https://docs.oracle.com/javase/tutorial/java/IandI/objectclass.html).

Généralement, des instances seront égales lorsque tous leurs attributs sont égaux (au sens de leur [méthode equals](https://docs.oracle.com/javase/tutorial/java/IandI/objectclass.html) lorsqu'il s'agit d'objets).

-   **Note:** Lorsqu'on [redéfinit equals, il faut aussi redéfinir hashcode](https://jmdoudoux.developpez.com/cours/developpons/java/chap-techniques_java.php#techniques_java-2) (cf. infra).


<a id="orgcf366b7"></a>

## hashCode

Les structures de données basées sur des index ([HashSet<E>](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html), [HashMap<K,V>](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)) utilisent un code numérique associé aux valeurs de éléments / clés stockées. Cette valeur numérique (retournée par la méthode [hashcode en java](https://fr.wikipedia.org/wiki/Java_hashCode())) doit avoir les deux propriétés suivantes :

-   **obligatoirement:** deux objets égaux (au sens de la [méthode equals](https://docs.oracle.com/javase/tutorial/java/IandI/objectclass.html)) doivent avoir la même valeur de hashcode.
-   **autant que possible:** on essaie d'éviter les *collisions*, c'est-à-dire qu'on essaie d'éviter que des objets qui ne sont pas égaux (toujours au sens de la [méthode equals](https://docs.oracle.com/javase/tutorial/java/IandI/objectclass.html)) aient la même valeur de hashcode.


<a id="org3268424"></a>

## Interface Comparable ou objet Comparator

Lorsque l'on utilise une structure de donnée ( [TreeSet<E>](https://docs.oracle.com/javase/8/docs/api/java/util/TreeSet.html), [TreeMap<K,V>](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html)) qui ordonne ses éléments / clés, celle-ci doit pouvoir effectuer des comparaisons selon un [ordre total](https://fr.wikipedia.org/wiki/Ordre_total). On définit pour cela des méthodes de comparaison qui retournent un entier négatif, nul ou positif suivant que la première instance soit inférieure, égale ou supérieure à la seconde.

Cela peut se faire de deux façons différentes en Java :

-   en définissant une relation d'ordre générale toujours valable pour toutes les instances en implémentant l'interface [Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html).
-   de façon spécifique à une utilisation dans une structure de donnée en définissant une classe implémentant l'interface [Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html) et en passant une instance de cette classe à la construction de la structure de données.


<a id="org9806d7f"></a>

# Interfaces

On a pu constater que plusieurs classes pouvaient offrir les mêmes *fonctionnalités*, avec des implémentations différentes. La *Programmation Orientée Objet* de Java permet de définir des [interfaces](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html) qui expriment ces fonctionnalités. En pratique, on manipulera les instances autant que possible selon une interface, afin de laisser libre la classe d'implémentation.

Par exemple, si l'on définit une fonction prenant en argument une liste, on aura intérêt à définir par exemple:

```java
public static void anyFunction(List<Integer> xs){
    /* implémentation */
}
```

Plutôt que :

```java
public static void anyFunction(ArrayList<Integer> xs){
    /* implémentation */
}
```

et ou

```java
public static void anyFunction(LinkedList<Integer> xs){
    /* implémentation */
}
```

Sous réserve que la fonction `anyfunction` n'utilise que des fonctionnalités communes à [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) et à [LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) et donc mises à déclarées dans l'interface [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html).


<a id="org21144ed"></a>

## List

[L'interface List est implémentée par de nombreuses classes](https://jmdoudoux.developpez.com/cours/developpons/java/chap-collections.php#collections-3) et à chaque fois que possible, on utilisera la classe concrète aussi peu que possible (i.e. à l'instanciation), par exemple en écrivant :

```java
List<String> myStrings = new ArrayList<String>();
```

ou

```java
List<String> myStrings = new LinkedList<String>();
```

plutôt que :

```java
ArrayList<String> myStrings = new ArrayList<String>();
```

ou

```java
LinkedList<String> myStrings = new LinkedList<String>();
```


<a id="orgb31047d"></a>

## Set

[L'interface Set fait partie d'une hiérarchies de classes](https://jmdoudoux.developpez.com/cours/developpons/java/chap-collections.php#collections-4) et on l'utilisera à chaque fois que possible, par exemple en écrivant :

```java
Set<String> myStrings = new HashSet<String>();
```

ou

```java
Set<String> myStrings = new TreeSet<String>();
```

plutôt que :

```java
HashSet<String> myStrings = new HashSet<String>();
```

ou

```java
TreeSet<String> myStrings = new TreeSet<String>();
```


<a id="orgc1efd1d"></a>

## Map

[L'interface Map fait partie d'une hiérarchie de classes](https://jmdoudoux.developpez.com/cours/developpons/java/chap-collections.php#collections-5) et on l'utilisera à chaque fois que possible, par exemple en écrivant :

```java
Map<String, Integer> stringToInt = new HashMap<String, Integer>();
```

ou

```java
Map<String, Integer> stringToInt = new TreeMap<String, Integer>();
```

plutôt que :

```java
HashMap<String, Integer> stringToInt = new HashMap<String, Integer>();
```

ou

```java
TreeMap<String, Integer> stringToInt = new TreeMap<String, Integer>();
```


<a id="orgb6cfcc6"></a>

## Collection

En fait, il y a quelques fonctionnalités qui sont communes à toutes les structures de données (notamment le fait de pouvoir la parcourir, savoir si elle est vide ou connaître sa taille). L'interface [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) permet d'exprimer ce niveau d'abstraction. Lorsque cela est possible, on aura donc intérêt à prendre les arguments en tant que [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) pour avoir le code le plus générique et réutilisable possible.

On peut par exemple parcourir n'importe quelle collection soit [avec un Iterator](https://www.baeldung.com/java-iterator), soit avec la boucle `for( X x : xs)` où `xs` est un `X[]` ou une `Collection<X>`.


<a id="org055a94e"></a>

# Webliographie

-   [Les collections](https://www.jmdoudoux.fr/java/dej/chap-collections.htm#collections)
-   [Tutorial officiel sur les collections](https://docs.oracle.com/javase/tutorial/collections/index.html)
-   [Complexité algorithmique (cf. performance) des structures de données standard en Java](https://www.baeldung.com/java-collections-complexity)
-   [Résumé des différentes collections et les complexités algorithmiques de leurs principales opérations](https://en.wikiversity.org/wiki/Java_Collections_Overview)
-   [Les interfaces Comparable et Comparator](http://www.iro.umontreal.ca/~dift1020/cours/ift1020/communs/Cours/C10/ComparableComparator.pdf)
-   [Comparators / Comparable on Baeldung](https://www.baeldung.com/java-comparator-comparable)

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> car toutes les classes
en Java [héritent](https://fr.wikipedia.org/wiki/H%C3%A9ritage_(informatique)) (cf.POO) de la classe `Object`.

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> Il y a une classe java.util.Stack, mais on ne
l'utilise plus car elle n'est pas performante.

<sup><a id="fn.3" class="footnum" href="#fnr.3">3</a></sup> c'est-à-đire que
si l'on essaie de mettre plusieurs fois des valeurs égales dans un tel
ensemble (*set*), elle ne sera présente qu'une seule fois.
