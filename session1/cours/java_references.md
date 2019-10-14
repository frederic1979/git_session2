- [Références en Java](#orgcbe35d9)
- [Égalité et identité](#orgf26834d)
  - [Contra. types primitifs](#org5f0ce4f)
    - [Déclaration](#org620a22a)
    - [Affectation](#org5174da6)
  - [Chaîne de caractères](#org2933f79)
    - [Déclaration](#org2745bf6)
    - [Affectation](#orgdda30fc)
    - [Affectations](#orgffeb6dd)
    - [Affectations 2](#orgc92a8f3)
  - [Tableaux](#orga8cdb99)
    - [Déclaration](#orgf8c388e)
    - [Affectation](#org30a317d)
    - [Affectations](#org10d2b16)
    - [Affectations 2](#orgd265112)
  - [Objets](#orge7c508d)
    - [Déclaration](#org52f3263)
    - [Affectation](#orga1a0827)
    - [Affectations](#orgcfa7ec1)
    - [Affectations 2](#org70b3dec)
    - [equals()](#org2856791)
- [Combinaisons](#orgc089778)
  - [Tableaux de tableaux](#org7993897)
    - [Déclaration](#org8e7f966)
    - [Initialisation partielle](#orgea8de6a)
    - [Initialisation](#org0683660)
    - [Affectation](#orgedeac54)
    - [Copie superficielle](#org5c4732c)
    - [Copie profonde](#org51daa00)
    - [Égalité](#orgf7797f2)
  - [Objets contenant des objets](#orgf915618)
    - [Déclaration](#org52eea6c)
    - [Affectations](#orgf9ee629)
    - [clone()](#org03f0b16)
    - [constructeur par copie](#org7e28897)
  - [Tableaux d'objets](#orgbb8348d)
- [Exercices](#org845a393)
  - [Tableau à deux dimensions de caractères](#orgec7a2ba)
  - [Tableaux à deux dimensions d'objets](#org001f456)



<a id="orgcbe35d9"></a>

# Références en Java

Tous les objets et tous les tableaux sont manipulés à travers des **références**. En fait, elles correspondent à l'adresse d'un objet ou d'un tableau.


<a id="orgf26834d"></a>

# Égalité et identité

Si 'deux' valeurs sont au même endroit en mémoire, il s'agit en fait de la même valeurs : elles sont **identiques**.


<a id="org5f0ce4f"></a>

## Contra. types primitifs

Des valeurs de types primitifs ne sont jamais **identiques**.


<a id="org620a22a"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int score; // not a local variable
```

Il y a un `int` en mémoire.

![img](img/ref-int-0.png)


<a id="org5174da6"></a>

### Affectation

```java
int score= 0;
int other= score;
```

`score` et `other` sont des `int` **égaux**.

![img](img/ref-int-1.png)


<a id="org2933f79"></a>

## Chaîne de caractères


<a id="org2745bf6"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
String firstname;
```

Il n'y a **AUCUNE** chaîne de caractères en mémoire.

![img](img/ref-string-0.png)


<a id="orgdda30fc"></a>

### Affectation

```java
String firstname= "Bernard";
```

![img](img/ref-string-1.png)


<a id="orgffeb6dd"></a>

### Affectations

```java
String firstname= "Bernard";
String other= firstname;
```

`firstname` et `other` sont des chaînes de caractères **identiques**.

![img](img/ref-string-2.png)


<a id="orgc92a8f3"></a>

### Affectations 2

```java
String firstname= "Bernard";
String other= firstname;
String another= "Ber"+"nard";
```

`firstname` et `other` sont **identiques** entre elles et seulement **égales** à `another`.

![img](img/ref-string-3.png)


<a id="orga8cdb99"></a>

## Tableaux


<a id="orgf8c388e"></a>

### Déclaration

Si l'on exécute le code suivant:

```java
int[] originalData;
```

Il n'y a **AUCUN** tableau en mémoire.

![img](img/ref-array-0.png)


<a id="org30a317d"></a>

### Affectation

```java
int[] originalData= {1,3,0};
```

![img](img/ref-array-1.png)


<a id="org10d2b16"></a>

### Affectations

```java
int[] originalData= {1,3,0};
int[] other= originalData;
```

`originalData` et `other` sont des tableaux **identiques**.

![img](img/ref-array-2.png)


<a id="orgd265112"></a>

### Affectations 2

```java
int[] originalData= {1,3,0};
int[] other= originalData;
int[] another= {1,3,0};// or with new int[] and assignments
```

`originalData` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-array-3.png)


<a id="orge7c508d"></a>

## Objets


<a id="org52f3263"></a>

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


<a id="orga1a0827"></a>

### Affectation

```java
Person customer= new Person("Clark", "Kent", 42);
```

![img](img/ref-object-1.png)


<a id="orgcfa7ec1"></a>

### Affectations

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
```

`customer` et `other` sont des objets **identiques**.

![img](img/ref-objects-2.png)


<a id="org70b3dec"></a>

### Affectations 2

```java
Person customer= new Person("Clark", "Kent", 42);
Person other= customer;
Person another= new Person("Clark", "Kent", 42);
```

`customer` et `other` sont **identiques** entre elles et seulement **égales** à `another`. Comment tester l'égalité ?

![img](img/ref-object-3.png)


<a id="org2856791"></a>

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


<a id="orgc089778"></a>

# Combinaisons


<a id="org7993897"></a>

## Tableaux de tableaux


<a id="org8e7f966"></a>

### Déclaration

Avec une simple déclaration, il n'y a **aucun** tableau en mémoire.

```java
int[][] data;
```

![img](img/ref-array2d-0.png)


<a id="orgea8de6a"></a>

### Initialisation partielle

Si l'on ne crée qu'un seul tableau, il n'y a qu'un tableau qui **pourra** contrenir des références vers des tableaux.

```java
int[][] data= new int[2][];
```

![img](img/ref-array2d-1.png)


<a id="org0683660"></a>

### Initialisation

Il faut initialiser chacune des cases de tableau de tableaux.

```java
int[][] data= new int[2][];
for(int i=0; i != data.length; ++i){
  data[i]= new int[2+i];
}
```

![img](img/ref-array2d-2.png)


<a id="orgedeac54"></a>

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


<a id="org5c4732c"></a>

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


<a id="org51daa00"></a>

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


<a id="orgf7797f2"></a>

### Égalité

Comment tester l'égalité ?


<a id="orgf915618"></a>

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


<a id="org52eea6c"></a>

### Déclaration

Encore une fois, la simple déclaration ne crée aucun objet.

```java
ProgrammingPair pair;
```

![img](img/ref-object-object-0.png)


<a id="orgf9ee629"></a>

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


<a id="org03f0b16"></a>

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


<a id="org7e28897"></a>

### constructeur par copie

```java
  public ProgrammingPair(ProgrammingPair other){
      driver= new Person(other.driver);
      navigator= new Person(other.navigator);
  }
```


<a id="orgbb8348d"></a>

## Tableaux d'objets

Écrire une classe `Seminar` qui comporte:

-   un attribut `coach` de type `Person`
-   un attribut `attendents` de type "tableau de Person"


<a id="org845a393"></a>

# Exercices


<a id="orgec7a2ba"></a>

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


<a id="org001f456"></a>

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
