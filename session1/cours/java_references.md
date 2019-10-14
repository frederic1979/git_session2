- [Références en Java](#org2c5b8cf)
- [Égalité et identité](#org07f1281)
  - [Contra. types primitifs](#orgd5eb6be)
    - [Déclaration](#org3969fd1)
    - [Affectation](#org238acd6)
  - [Chaîne de caractères](#org189bd3f)
    - [Déclaration](#orgbd403ca)
    - [Affectation](#org7fcdb3a)
    - [Affectations](#org66b8bdd)
    - [Affectations 2](#org4ad52fa)
  - [Tableaux](#orgb1baaac)
    - [Déclaration](#orgc2a6589)
    - [Affectation](#org5678a97)
    - [Affectations](#orgd68c33e)
    - [Affectations 2](#org3e973b8)
  - [Objets](#org7f87082)
    - [Déclaration](#org44ef336)
    - [Affectation](#orgbfa87b5)
    - [Affectations](#org4b78f2d)
    - [Affectations 2](#orga730ea7)
    - [equals()](#org59664c4)
- [Combinaisons](#org5200f32)
  - [Tableaux de tableaux](#org14cb245)
    - [Déclaration](#org935d5e9)
    - [Initialisation partielle](#org84e0ce9)
    - [Initialisation](#org1574175)
    - [Affectation](#orgfb7036d)
    - [Copie superficielle](#org6a9ce1b)
    - [Copie profonde](#org63d9ee7)
    - [Égalité](#org8f0b95f)
  - [Objets contenant des objets](#orgcb56dd3)
    - [Déclaration](#org9084a1f)
    - [Affectations](#orgb5c0450)
    - [clone()](#org9134557)
    - [constructeur par copie](#org243c557)
  - [Tableaux d'objets](#org9df0c06)
- [Exercices](#orgee3a69f)
  - [Tableau à deux dimensions de caractères](#org8882139)
  - [Tableaux à deux dimensions d'objets](#orgf6e77ca)



<a id="org2c5b8cf"></a>

# Références en Java

Tous les objets et tous les tableaux sont manipulés à travers des **références**. En fait, elles correspondent à l'adresse d'un objet ou d'un tableau.


<a id="org07f1281"></a>

# Égalité et identité

Si 'deux' valeurs sont au même endroit en mémoire, il s'agit en fait de la même valeurs : elles sont **identiques**.


<a id="orgd5eb6be"></a>

## Contra. types primitifs

Des valeurs de types primitifs ne sont jamais **identiques**.


<a id="org3969fd1"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int score; // not a local variable
```

Il y a un `int` en mémoire.

![img](img/ref-int-0.png)


<a id="org238acd6"></a>

### Affectation

```java
int score= 0;
int other= score;
```

`score` et `other` sont des `int` **égaux**.

![img](img/ref-int-1.png)


<a id="org189bd3f"></a>

## Chaîne de caractères


<a id="orgbd403ca"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
String firstname;
```

Il n'y a **AUCUNE** chaîne de caractères en mémoire.

![img](img/ref-string-0.png)


<a id="org7fcdb3a"></a>

### Affectation

```java
String firstname= "Bernard";
```

![img](img/ref-string-1.png)


<a id="org66b8bdd"></a>

### Affectations

```java
String firstname= "Bernard";
String other= firstname;
```

`firstname` et `other` sont des chaînes de caractères **identiques**.

![img](img/ref-string-2.png)


<a id="org4ad52fa"></a>

### Affectations 2

```java
String firstname= "Bernard";
String other= firstname;
String another= "Ber"+"nard";
```

`firstname` et `other` sont **identiques** entre elles et seulement **égales** à `another`.

![img](img/ref-string-3.png)


<a id="orgb1baaac"></a>

## Tableaux


<a id="orgc2a6589"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int[] originalData;
```

Il n'y a **AUCUN** tableau en mémoire.

![img](img/ref-array-0.png)


<a id="org5678a97"></a>

### Affectation

```java
int[] originalData= {1,3,0};
```

![img](img/ref-array-1.png)


<a id="orgd68c33e"></a>

### Affectations

```java
int[] originalData= {1,3,0};
int[] other= originalData;
```

`originalData` et `other` sont des tableaux **identiques**.

![img](img/ref-array-2.png)


<a id="org3e973b8"></a>

### Affectations 2

```java
int[] originalData= {1,3,0};
int[] other= originalData;
int[] another= {1,3,0};// or with new int[] and assignments
```

`originalData` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-array-3.png)


<a id="org7f87082"></a>

## Objets


<a id="org44ef336"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
  public class Person{
      String firstname;
      String lastname;
      int age;
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


<a id="orgbfa87b5"></a>

### Affectation

```java
Person customer= new Person("Clark", "Kent", 42);
```

![img](img/ref-object-1.png)


<a id="org4b78f2d"></a>

### Affectations

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
```

`customer` et `other` sont des objets **identiques**.

![img](img/ref-objects-2.png)


<a id="orga730ea7"></a>

### Affectations 2

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
Person another= new Person("Clark", "Kent", 42);
```

`customer` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-object-3.png)


<a id="org59664c4"></a>

### equals()

On redéfini la méthode [equals(Object other)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-):

```java
  public class Person{
      String firstname;
      String lastname;
      int age;
      public Person(String firstname, String lastname, int age){
	  this.firstname= firstname;
	  this.lastname= lastname;
	  this.age= age;
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


<a id="org5200f32"></a>

# Combinaisons


<a id="org14cb245"></a>

## Tableaux de tableaux


<a id="org935d5e9"></a>

### Déclaration

Avec une simple déclaration, il n'y a **aucun** tableau en mémoire.

```java
int[][] data;
```

![img](img/ref-array2d-0.png)


<a id="org84e0ce9"></a>

### Initialisation partielle

Si l'on ne crée qu'un seul tableau, il n'y a qu'un tableau qui **pourra** contrenir des références vers des tableaux.

```java
int[][] data= new int[2][];
```

![img](img/ref-array2d-1.png)


<a id="org1574175"></a>

### Initialisation

Il faut initialiser chacune des cases de tableau de tableaux.

```java
int[][] data= new int[2][];
for(int i=0; i != data.length; ++i){
  data[i]= new int[2+i];
}
```

![img](img/ref-array2d-2.png)


<a id="orgfb7036d"></a>

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


<a id="org6a9ce1b"></a>

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


<a id="org63d9ee7"></a>

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


<a id="org8f0b95f"></a>

### Égalité

Comment tester l'égalité ?


<a id="orgcb56dd3"></a>

## Objets contenant des objets

Soit la classe (problématique) suivante :

```java
public class ProgrammingPair {
  Person driver;
  Person navigator;
  public Person getDriver(){ return driver;}
  public void setDriver(Person driver){ this.driver= driver;}
  public Person getNavigator(){ return navigator;}
  public void setNavigator(Person navigator){ this.navigator= navigator;}

}
```


<a id="org9084a1f"></a>

### Déclaration

Encore une fois, la simple déclaration ne crée aucun objet.

```java
ProgrammingPair pair;
```

![img](img/ref-object-object-0.png)


<a id="orgb5c0450"></a>

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
ProgrammingPair other= originalPair;
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


<a id="org9134557"></a>

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

![img](img/ref-object-object-3.png)

En fait, on utilise plutôt [un constructeur par copie](https://www.artima.com/intv/bloch13.html).


<a id="org243c557"></a>

### constructeur par copie

```java
  public ProgrammingPair(ProgrammingPair other){
      driver= new Person(other.driver);
      navigator= new Person(other.navigator);
  }
```


<a id="org9df0c06"></a>

## Tableaux d'objets

Écrire une classe `Seminar` qui comporte:

-   un attribut `coach` de type `Person`
-   un attribut `attendents`= de type "tableau de Person"


<a id="orgee3a69f"></a>

# Exercices


<a id="org8882139"></a>

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


<a id="orgf6e77ca"></a>

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
