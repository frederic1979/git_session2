- [Principe](#org69d6ab9)
- [Classe et objet](#org8ef95cf)
- [Classes en Java](#org6173e29)
- [Packages](#org79b7510)
- [Interface et implémentation](#orgd3fd615)
- [Minimisation de la compléxité](#org6af9a03)
- [Visibilités](#orgcd11bb7)
- [Mot clé `static`](#org85a2bc8)
- [Attributs de classe](#orgfb7f95a)
- [Attributs constants](#orgb171259)
  - [En pratique 1/2](#org44d2f83)
  - [En pratique 2/2](#orga819159)
- [Objets](#orgbe93532)
- [Constructeurs](#org2fc45b5)
  - [mot clé `this`](#org252a1ac)
- [Accesseurs](#orgc10585e)
- [Méthodes](#org37d24b9)
- [equals et toString](#org8d1739c)
- [Références](#org4e8023f)
- [Classes immutables](#org9518245)
- [En pratique 1/2](#orgff62dc0)
  - [Classe QuizzItem immutable](#orgb684f76)
  - [Classe QuizzItem mutable](#orgf84d0f9)
  - [Instances de la classe Quizz](#org2ce45e9)



<a id="org69d6ab9"></a>

# Principe

Un programme est constitué de données et de code manipulant ces données. Les classes sont des unités de décomposition de données et du code qui les manipule.


<a id="org8ef95cf"></a>

# Classe et objet

-   Une classe est le type d'un objet.

-   Un objet est une instance d'une classe


<a id="org6173e29"></a>

# Classes en Java

En Java, tout le code est implémenté sous forme de classes.


<a id="org79b7510"></a>

# Packages

Les packages sont l'organisation hiérarchique des classes (cf. répertoires pour les fichiers).

On peut utiliser un nom complètement qualifié (*fully qualified name*) `java.util.Scanner` ou utiliser des directives `import` : `import java.util.Scanner;` ou `import java.util.*;`.

-   **Exercices:** -   Créer une classe dans un package
    -   Dans un programme existant, utiliser une classe par son nom complètement qualifié, puis avec un `import` spécifique, puis avec un `import` de tout le contenu d'un *package*.


<a id="orgd3fd615"></a>

# Interface et implémentation

-   Interface : "quoi" / ce qui est visible
-   Implémentation : "comment" / ce qui est caché

On parle d'*encapsulation*.

-   **Exemples:** -   ajouter un élément dans un ensemble ([Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)), [indexé](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html) ou [ordonné](https://docs.oracle.com/javase/8/docs/api/java/util/TreeSet.html), associer une valeur à une clé dans une table d'association ([Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)), [indexée](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html) ou [ordonnée](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html).
    -   récupérer des informations sur une erreur ([Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getMessage--) dont les plus connues sont les [Exceptions](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)), par exemple pour une erreur d'indice ([IndexOutOfBoundsException](https://docs.oracle.com/javase/8/docs/api/java/lang/IndexOutOfBoundsException.html)) qui indiquera la valeur d'indice erronée ou pour une erreur d'accès à un fichier ([FileNotFoundException](https://docs.oracle.com/javase/8/docs/api/java/io/FileNotFoundException.html)) qui indiquera le nom du fichier problématique.

-   **Exercices:** Comparer les *signatures* des méthodes :
    -   `put` de `java.util.Map`, `java.util.HashMap` et `java.util.TreeMap`
    
    -   `getMessage` de `IndexOutOfBoundsException` et `FileNotfoundException`.


<a id="org6af9a03"></a>

# Minimisation de la compléxité

On minimise ce qui est visible : il n'y a pas de dépendance envers ce qui n'est pas visible (&rarr; possibilité d'évolutions).


<a id="orgcd11bb7"></a>

# Visibilités

Les différents [niveaux de visibilité](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) indiquent quel code a accès à ce qui est qualifié:

| qualificatif | Classe | Package | Sous-classe | Tout |
|------------ |------ |------- |----------- |---- |
| `public`     | ✓      | ✓       | ✓           | ✓    |
| `protected`  | ✓      | ✓       | ✓           |      |
|              | ✓      | ✓       |             |      |
| `private`    | ✓      |         |             |      |

(sous-classe &rarr; cf. infra héritage)

-   **Exercices:** -   Créer une classe `VisiP` sans qualificatif de visibilité dans un package `co.simplon.p1` avec une fonction :
        
        ```java
        static void message(){
            System.out.println("Hello from VisiP !");
        }
        ```
    -   Créer une classe `Main` dans un package `co.simplon.p1` avec une fonction `public static void main(String[] args)` qui essaie d'appeler `VisiP.message()`.
    -   Que se passe-t'il si `Main` est dans un package `co.simplon` ? Quelle(s) modification(s) faut-il faire ?


<a id="org85a2bc8"></a>

# Mot clé `static`

Ce qui est qualifié de `static` concerne la classe (n'est pas créé en cours d'exécution). Cf. `public static vois main(String[] args)`.


<a id="orgfb7f95a"></a>

# Attributs de classe

On peut associer des données à une classe avec des *attributs*. Ceux-ci sont accessibles, selon leur visibilité, comme des variables avec une durée de vie qui est celle du programme. On accède à un attribut d'une classe comme à une fonction (*méthode*) de classe:

```java
System.out;
Integer.MAX_VALUE;
```


<a id="orgb171259"></a>

# Attributs constants

En fait, pour limiter le *couplage* on utilise généralement des attributs de classe qui sont déclarés constant :

```java
public static final int NB_OF_RETRIES= 3;
```


<a id="org44d2f83"></a>

## En pratique 1/2

Dans la classe `VisiP`, mettre un attribut de classe `GREETING` de type `String` pour remplacer le `"hello"` de la classe `VisiP`.


<a id="orga819159"></a>

## En pratique 2/2

Modifier la classe `Quizz` pour que la fonction `main` soit comme suit :

```java
  public static void main(String[] args){
   for(int i=0; i != questions.length; ++i){
       System.out.println(questions[i]);
       String answer= in.nextLine();
       if(answer.equals(answers[i])){
	   score+= scores[i];
       }
   }
   displayResult();
  }
```


<a id="orgbe93532"></a>

# Objets

Lorsque l'on veut manipuler différents *valeurs* pour un même type composé, l'on doit *instancier* la classe décrivant ce type:

```java
  public class TestItem {
      String question;
      String answer;
      int points;
  }
```

On utilise le mot-clé `new` :

```java
TestItem ti= new TestItem();
```


<a id="org2fc45b5"></a>

# Constructeurs

On initialise les *attributs* d'un objet à l'occasion de la *construction* d'un objet. Dans une méthode d'instance (et un constructeur) on peut accéder directement aux attributs de l'instance.

```java
  public class TestItem {
      public TestItem(String q, String a, int p){
	  question= q;
	  answer= a;
	  points= p;
      }
  }
```


<a id="org252a1ac"></a>

## mot clé `this`

On peut aussi préfixer avec le mot-clé `this` :

```java
  public class TestItem {
      public TestItem(String question, String answer, int points){
	  this.question= question;
	  this.answer= answer;
	  this.points= points;
      }
  }
```


<a id="orgc10585e"></a>

# Accesseurs

Généralement, on ne permet pas l'accès direct aux attributs, mais l'on utilise **si nécessaire** des *accesseurs* : *getter* et *setter* :

```java
public TypeOfXXX getXXX(){
  return xxx;
}
public void setXXX( TypeOfXXX xxx ){
  this.xxx= xxx;
}
```


<a id="org37d24b9"></a>

# Méthodes

Une méthode d'instance (non qualifiée par `static`) :

-   est appelée sur une instance
    
    ```java
      System.out.println();
      str.equals("test");
    ```
-   a accès implicite aux attributs d'instance (Cf. accesseurs)


<a id="org8d1739c"></a>

# equals et toString

On réimplémente (cf. infra héritage) généralement au moins les méthodes [equals](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-) et [toString](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--). Cette dernière est appellée automatiquement lors d'une concaténation ou d'un affichage avec `println`.


<a id="org4e8023f"></a>

# Références

En fait, tous les objets sont manipulés par références (comme les instances de `String`, `Integer`,…).

Cf. implications pour arguments, ==, …


<a id="org9518245"></a>

# Classes immutables

Si tous les attributs d'instance sont constants, il n'y a pas de risques de modifications problématiques.


<a id="orgff62dc0"></a>

# En pratique 1/2

Modifier le programme `Quizz` pour utiliser des objets d'une classe `TestItem`.


<a id="orgb684f76"></a>

## Classe QuizzItem immutable

Utiliser une classe `QuizzItem` immutable, avec une méthode qui retourne le nombre de points obtenus en validant ou non une réponse proposée.


<a id="orgf84d0f9"></a>

## Classe QuizzItem mutable

Utiliser une classe `QuizzItem` mutable avec un attribut qui permette de reproposer la question en cas de réponse erronée.


<a id="org2ce45e9"></a>

## Instances de la classe Quizz

Modifier la classe `Quizz` pour que le main instancie un objet paramétré par le nombre d'essais:

```java
  public static void main(String[] args){
      Quizz session= new Quizz(nbRetries);
      session.doTest();
      session.displayResults();
  }
```
