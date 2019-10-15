- [Références en Java](#org055d491)
- [Égalité et identité](#org983cf74)
  - [Contra. types primitifs](#org5299378)
    - [Déclaration](#org30fbe99)
    - [Affectation](#org72a4d1b)
  - [Chaîne de caractères](#org417057f)
    - [Déclaration](#org57df6cd)
    - [Affectation](#org732eb03)
    - [Affectations](#org69c37d3)
    - [Affectations 2](#orgd0dc903)
  - [Tableaux](#orgfd2240b)
    - [Déclaration](#orgd27c620)
    - [Affectation](#org46cb4e6)
    - [Affectations](#org656322e)
    - [Affectations 2](#orgdd966af)
  - [Objets](#org545936a)
    - [Déclaration](#org89564de)
    - [Affectation](#orga56d1f0)
    - [Affectations](#org45887f3)
    - [Affectations 2](#org62d5082)
    - [equals()](#orgc1a0ee4)
- [Combinaisons](#orge9a4d1a)
  - [Tableaux de tableaux](#orgdc1809d)
    - [Déclaration](#org3e07355)
    - [Initialisation partielle](#org5201ab1)
    - [Initialisation](#orgf278374)
    - [Affectation](#org907ae06)
    - [Copie superficielle](#org882251b)
    - [Copie profonde](#org62ba583)
    - [Égalité](#orgaa1643f)
  - [Objets contenant des objets](#orgab8b46f)
    - [Déclaration](#orge359fe4)
    - [Affectations](#orga01e863)
    - [clone()](#orga391d8b)
    - [constructeur par copie](#org6ab9539)
  - [Remarque sur les objets de classes immuables](#orgb0ee390)
  - [equals()](#orgb7213db)
  - [Tableaux d'objets](#org2e0f9ee)
- [Exercices](#org0729b55)
  - [Tableau à deux dimensions de caractères](#org5d93dc5)
  - [Tableaux à deux dimensions d'objets](#org4ee89db)



<a id="org055d491"></a>

# Références en Java

Tous les objets et tous les tableaux sont manipulés à travers des **références**. En fait, elles correspondent à l'adresse d'un objet ou d'un tableau.


<a id="org983cf74"></a>

# Égalité et identité

Si 'deux' valeurs sont au même endroit en mémoire, il s'agit en fait de la même valeurs : elles sont **identiques**.


<a id="org5299378"></a>

## Contra. types primitifs

Des valeurs de types primitifs ne sont jamais **identiques**.


<a id="org30fbe99"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int score; // not a local variable
```

Il y a un `int` en mémoire.

![img](img/ref-int-0.png)


<a id="org72a4d1b"></a>

### Affectation

```java
int score= 0;
int other= score;
```

`score` et `other` sont des `int` **égaux**.

![img](img/ref-int-1.png)


<a id="org417057f"></a>

## Chaîne de caractères


<a id="org57df6cd"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
String firstname;
```

Il n'y a **AUCUNE** chaîne de caractères en mémoire.

![img](img/ref-string-0.png)


<a id="org732eb03"></a>

### Affectation

```java
String firstname= "Bernard";
```

![img](img/ref-string-1.png)


<a id="org69c37d3"></a>

### Affectations

```java
String firstname= "Bernard";
String other= firstname;
```

`firstname` et `other` sont des chaînes de caractères **identiques**.

![img](img/ref-string-2.png)


<a id="orgd0dc903"></a>

### Affectations 2

```java
String firstname= "Bernard";
String other= firstname;
String another= "Ber"+"nard";
```

`firstname` et `other` sont **identiques** entre elles et seulement **égales** à `another`.

![img](img/ref-string-3.png)


<a id="orgfd2240b"></a>

## Tableaux


<a id="orgd27c620"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int[] originalData;
```

Il n'y a **AUCUN** tableau en mémoire.

![img](img/ref-array-0.png)


<a id="org46cb4e6"></a>

### Affectation

```java
int[] originalData= {1,3,0};
```

![img](img/ref-array-1.png)


<a id="org656322e"></a>

### Affectations

```java
int[] originalData= {1,3,0};
int[] other= originalData;
```

`originalData` et `other` sont des tableaux **identiques**.

![img](img/ref-array-2.png)


<a id="orgdd966af"></a>

### Affectations 2

```java
int[] originalData= {1,3,0};
int[] other= originalData;
int[] another= {1,3,0};// or with new int[] and assignments
```

`originalData` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-array-3.png)


<a id="org545936a"></a>

## Objets


<a id="org89564de"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
  public class Person{
      private String firstname;
      private String lastname;
      private int age;
      public Person(String firstname, String lastname, int age){
	  this.firstname= firstname;
	  this.lastname= lastname;
	  this.age= age;
      }
  }
```

```java
Person customer;
```

Il n'y a **AUCUN** objet de classe `Person` en mémoire.

![img](img/ref-object-0.png)


<a id="orga56d1f0"></a>

### Affectation

```java
Person customer= new Person("Clark", "Kent", 42);
```

![img](img/ref-object-1.png)


<a id="org45887f3"></a>

### Affectations

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
```

`customer` et `other` sont des objets **identiques**.

![img](img/ref-objects-2.png)


<a id="org62d5082"></a>

### Affectations 2

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
Person another= new Person("Clark", "Kent", 42);
```

`customer` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-object-3.png)


<a id="orgc1a0ee4"></a>

### equals()

On redéfini la méthode [equals(Object other)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-):

```java
public class Person{
    private String firstname;
    private String lastname;
    private int age;

    public Person(String firstname, String lastname, int age){
	this.firstname= firstname;
	this.lastname= lastname;
	this.age= age;
    }
    public Person(Person other){
	this(other.firstname, other.lastname, other.age);
    }
    public boolean equals(Object other){
	if(other != null && (other instanceof Person)){
	    Person otherPerson= (Person) other;
	    if(firstname.equals(otherPerson.firstname) 
	       && lastname.equals(otherPerson.lastname)
	       && (age == otherPerson.age)){
		return true;
	    }
	}
	return false;
    }
}
```

Analyser et comprendre chacune des opérations de cette méthode.


<a id="orge9a4d1a"></a>

# Combinaisons


<a id="orgdc1809d"></a>

## Tableaux de tableaux


<a id="org3e07355"></a>

### Déclaration

Avec une simple déclaration, il n'y a **aucun** tableau en mémoire.

```java
int[][] data;
```

![img](img/ref-array2d-0.png)


<a id="org5201ab1"></a>

### Initialisation partielle

Si l'on ne crée qu'un seul tableau, il n'y a qu'un tableau qui **pourra** contrenir des références vers des tableaux.

```java
int[][] data= new int[2][];
```

![img](img/ref-array2d-1.png)


<a id="orgf278374"></a>

### Initialisation

Il faut initialiser chacune des cases de tableau de tableaux.

```java
int[][] data= new int[2][];
for(int i=0; i != data.length; ++i){
  data[i]= new int[2+i];
}
```

![img](img/ref-array2d-2.png)


<a id="org907ae06"></a>

### Affectation

Si l'on ne crée pas d'autres tableaux, il n'y a pas d'autre tableau !

```java
int[][] data= new int[2][];
for(int i=0; i != data.length; ++i){
  data[i]= new int[2+i];
}
int [][] other= data;
```

![img](img/ref-array2d-3.png)


<a id="org882251b"></a>

### Copie superficielle

Si l'on ne copie que le tableau de tableaux, seul celui-ci est recopié, pas son contenu.

```java
int[][] data= new int[2][];
for(int i=0; i != data.length; ++i){
  data[i]= new int[2+i];
}
int [][] other= new int[data.length][];
for(int i=0; i != data.length; ++i){
  other[i]= data[i];
}
```

![img](img/ref-array2d-4.png)


<a id="org62ba583"></a>

### Copie profonde

```java
  public static int[][] deepCopy(int[][] data){
      int [][] result= new int[data.length][];
      for(int i=0; i != data.length; ++i){
	  result[i]= new int[data[i].length];
	  for(int =0; j != data[i].length; ++j){
	      result[i][j]= data[i][j];
	  }
      }
      return result;
  }
```

![img](img/ref-array2d-5.png)


<a id="orgaa1643f"></a>

### Égalité

Comment tester l'égalité ?


<a id="orgab8b46f"></a>

## Objets contenant des objets

Soit la classe (problématique) suivante :

```java
public class ProgrammingPair {
  private Person driver;
  private Person navigator;
  public Person getDriver(){ return driver;}
  public void setDriver(Person driver){ this.driver= driver;}
  public Person getNavigator(){ return navigator;}
  public void setNavigator(Person navigator){ this.navigator= navigator;}

}
```


<a id="orge359fe4"></a>

### Déclaration

Encore une fois, la simple déclaration ne crée aucun objet.

```java
ProgrammingPair pair;
```

![img](img/ref-object-object-0.png)


<a id="orga01e863"></a>

### Affectations

```java
ProgrammingPair pair= new ProgrammingPair();
```

![img](img/ref-object-object-1.png)

```java
ProgrammingPair pair= new ProgrammingPair();
pair.setDriver(new Person("Clark", "Kent", 42));
pair.setNavigator(new Person("Lex", "Luthor", 45));
```

![img](img/ref-object-object-2.png)

```java
ProgrammingPair pair= new ProgrammingPair();
pair.setDriver(new Person("Clark", "Kent", 42));
pair.setNavigator(new Person("Lex", "Luthor", 45));
ProgrammingPair other= pair;
```

![img](img/ref-object-object-3.png)

```java
ProgrammingPair pair= new ProgrammingPair();
pair.setDriver(new Person("Clark", "Kent", 42));
pair.setNavigator(new Person("Lex", "Luthor", 45));
ProgrammingPair other= new ProgrammingPair();
other.setDriver(pair.getDriver());
other.setNavigator(pair.getNavigator());
```

![img](img/ref-object-object-4.png)


<a id="orga391d8b"></a>

### clone()

Pour construire un nouvel objet qui est une copie, il a été conventionnel d'utiliser une méthode `clone`.

```java
  public ProgrammingPair clone(){
      return new ProgrammingPair(driver, navigator); // this cstor should exist anyway !
  }
```

```java
ProgrammingPair pair= new ProgrammingPair("Clark", "Kent", 42);
ProgrammingPair other= pair.clone();
```

En fait, on utilise plutôt [un constructeur par copie](https://www.artima.com/intv/bloch13.html).


<a id="org6ab9539"></a>

### constructeur par copie

```java
  public ProgrammingPair(ProgrammingPair other){
      driver= new Person(other.driver);
      navigator= new Person(other.navigator);
  }
```

![img](img/ref-object-object-copy-cstor.png)


<a id="orgb0ee390"></a>

## Remarque sur les objets de classes immuables

L'intérêt de créer des copies, plutôt que de partager des références sur des objets identiques, est d'assurer l'indépendance entre la copie et l'original : aucune modification de l'un n'aura d'impacts sur l'autre.

Dans le cas d'objets qui ne peuvent pas être modifiés car ils sont des instances de classes *immuables* (*immutable*), il n'y a pas d'inconvénients à avoir des objets identiques. Ainsi, on considère la copie de instances des classes `ProgrammingPair` et des classes `Person` comme profondes même si les attributs contiennent des références vers des objets de classe `String` identiques :

![img](img/ref-object-object-copy-cstor-str.png)


<a id="orgb7213db"></a>

## equals()

On doit aussi redéfinir la méthode `public boolean equals(Object other)` :

```java
public boolean equals(Object other){
    if((other == null) || !(other instanceof ProgrammingPair)){
	return false;
    }
    ProgrammingPair otherProgrammingPair = (ProgrammingPair) other;
    return driver.equals(otherProgrammingPair.driver)
	&& navigator.equals(otherProgrammingPair.navigator);
}

```


<a id="org2e0f9ee"></a>

## Tableaux d'objets

Écrire une classe `Seminar` qui comporte:

-   un attribut `coach` de type `Person`
-   un attribut `attendents` de type "tableau de Person"

```java
import java.util.Arrays;

public class Seminar {
    private Person coach;
    private Person[] attendants;

    public Seminar(Person coach, Person[] attendants){
	this.coach = new Person(coach);
	this.attendants = new Person[attendants.length];
	for(int i=0; i != attendants.length; ++i){
	    this.attendants[i] = new Person(attendants[i]);
	}
    }
    public Seminar(Seminar other){
	this(other.coach, other.attendants);
    }
/*    public boolean equals(Object other){
	if((other == null) || !(other instanceof Seminar)){
	    return false;
	}
	Seminar otherSeminar = (Seminar)other;
	return coach.equals(otherSeminar.coach)
	    && Arrays.deepEquals(attendants, otherSeminar.attendants);
	// on peut faire Arrays.equals(attendants, otherSeminar.attendants)
	// on NE PEUT PAS faire attendants.equals(otherSeminar.attendants) !!!
    }
*/
    public boolean equals(Object other){
	if((other == null) || !(other instanceof Seminar)){
	    return false;
	}
	Seminar otherSeminar = (Seminar)other;
	boolean res = coach.equals(otherSeminar.coach);
	res &= attendants.length == otherSeminar.attendants.length;
	for(int i=0;  res && (i != attendants.length); ++i){
	    res &= attendants[i].equals(otherSeminar.attendants[i]);
	}
	return res;
    }
}
```


<a id="org0729b55"></a>

# Exercices


<a id="org5d93dc5"></a>

## Tableau à deux dimensions de caractères

Que fait le programme suivant ? Pourquoi ? Comment le corriger (pour qu'il affiche une croix) ?

```java
public class DebugArr2D {
    public static char[] initializedArray(char c, int nb){
	char[] res= new char[nb];
	for(int i=0; i != res.length; ++i){
	    res[i]= c;
	}
	return res;
    }
    public static char[][] initializedArray2D(char[] arr, int nb){
	char[][] res= new char[nb][];
	for(int i=0; i != res.length; ++i){
	    res[i]= arr;
	}
	return res;
    }
    public static void display(char[][] arr2D){
	for(char[] row : arr2D){
	    for(char c : row){
		System.out.print(c);
	    }
	    System.out.println();
	}
    }
    public static void main(String[] args){
	char[][] screen= initializedArray2D(initializedArray(' ', 20), 20);
	for(int i= 0; i != Math.min(screen.length, screen[0].length); ++i){
	    screen[i][i]='X';
	    screen[screen.length-i-1][i]='X';
	}
	display(screen);
    }
}
```


<a id="org4ee89db"></a>

## Tableaux à deux dimensions d'objets

Que fait le programme suivant ? Pourquoi ? Comment le corriger (pour qu'il affiche une croix) ?

```java
class Stone{
    private boolean firstPlayer;
    public Stone(boolean firstPlayer) {
	this.firstPlayer= firstPlayer;
    }
    public boolean isFirstPlayer() {
	return firstPlayer;
    }
    public void setFirstPlayer(boolean firstPlayer) {
	this.firstPlayer= firstPlayer;
    }
    public String toString() {
	return firstPlayer ? "O":"X";
    }
}
```

```java
public class DebugArray2DObjects {
    public static Stone[] initializedArray(Stone s, int nb){
	Stone[] res= new Stone[nb];
	for(int i=0; i != res.length; ++i){
	    res[i]= s;
	}
	return res;
    }
    public static Stone[][] initializedArray2D(Stone[] arr, int nb){
	Stone[][] res= new Stone[nb][];
	for(int i=0; i != res.length; ++i){
	    res[i]= arr;
	}
	return res;
    }
    public static void display(Stone[][] board){
	for(Stone[] row : board){
	    for(Stone c : row){
		System.out.print(c);
	    }
	    System.out.println();
	}
    }
    public static void main(String[] args){
	Stone[][] screen= initializedArray2D(initializedArray(new Stone(false), 20), 20);
	for(int i= 0; i != Math.min(screen.length, screen[0].length); ++i){
	    screen[i][i].setFirstPlayer(true);
	    screen[screen.length-i-1][i].setFirstPlayer(true);
	}
	display(screen);
    }
}
```
