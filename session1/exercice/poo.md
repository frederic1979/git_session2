- [Objectifs](#orgda26ac9)
- [Préliminaires](#orgcaff152)
- [Permettre les tests d'égalité entre instances](#org58dc5e6)
  - [Définir une méthode equals(Person p)](#org035629e)
  - [Définir une méthode equals(Object o)](#org2c461dc)
- [Permettre l'affichage du contenu d'une instance](#org233b741)
- [Implémentation d'interface](#orga6ba42e)
  - [Implémentation de l'interface Comparable](#org0d1ea87)
  - [Implémentation de l'interface Comparable<Person>](#org732fcf4)



<a id="orgda26ac9"></a>

# Objectifs

Pratiquer la redéfinition de méthodes et l'implémentation d'interfaces.


<a id="orgcaff152"></a>

# Préliminaires

Créer une classe Person :

![img](Person.png)

Avec un constructeur qui permette d'initialiser les attributs.


<a id="org58dc5e6"></a>

# Permettre les tests d'égalité entre instances


<a id="org035629e"></a>

## Définir une méthode equals(Person p)

On pourrait être tenté de définir une méthode `public boolean equals(Person p)`.

Définir une telle méthode et essayer de l'utiliser :

```java
    Person p1 = new Person ("Bernard", "h");
    Person p2 = new Person("Bernard", "h");
    System.out.println(p1.equals(p2));
```

Puis comme ceci :

```java
    Object p1 = new Person ("Bernard", "h");
    Object p2 = new Person("Bernard", "h");
    System.out.println(p1.equals(p2));
```

Expliquer le deuxième résultat.

On a voulu redéfinir la méthode `equals` définie dans la classe [Object](https://docs.oracle.com/javase/10/docs/api/java/lang/Object.html). On peut indiquer cette intention de *redéfinir* une méthode avec l'[annotation @Override](https://www.baeldung.com/java-override). Qualifier la méthode `public boolean equals(Person p)` avec l'annotation `@Override` : que se passe-t-il ?


<a id="org2c461dc"></a>

## Définir une méthode equals(Object o)

Il faut se persuader que le deuxième cas de figure (lorsque l'on manipule un objet de classe `Person` à travers une référence de classe `Object` qui est la plus utile ! En effet, à chaque fois qu'une classe déjà existante (par exemple les structures de données de la bibliothèque standard Java (e.g. `ArrayList` ou `TreeSet`), elle ne peut évidemment pas avoir été écrite ou même compilée en prenant en compte notre nouvelle classe. On doit donc pouvoir gérer ce cas de figure, en redéfinissant vraiment (et non en surchargeant) la méthode [equals](https://docs.oracle.com/javase/10/docs/api/java/lang/Object.html#equals(java.lang.Object)) définie dans la classe [Object](https://docs.oracle.com/javase/10/docs/api/java/lang/Object.html).

Redéfinir la méthode `public boolean equals(Object o)`. Vérifier que le code suivant donne cette fois-ci le résultat attendu :

```java
    Object p1 = new Person ("Bernard", "h");
    Object p2 = new Person("Bernard", "h");
    System.out.println(p1.equals(p2));
```


<a id="org233b741"></a>

# Permettre l'affichage du contenu d'une instance

Si l'on passe une instance de la classe `Person` en argument de la méthode [print](https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#print(java.lang.Object)) (ou [println](https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#println(java.lang.Object))) de `System.out`, le résultat est décevant. Aussi décevant que lorsqu'on passait des tableaux en espérant voir afficher leur contenu. En fait, la méthode [print](https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#print(java.lang.Object)) (ou [println](https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#println(java.lang.Object))) va utiliser le résultat de la méthode [toString](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#toString()) définie dans la classe [Object](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html).

Faire en sorte que l'affichage des instances de la classe `Person` affiche le nom et le prénom.


<a id="orga6ba42e"></a>

# Implémentation d'interface

On voudra désormais en plus être capable d'ordonner des instances de notre classe `Person` (ordre alphabétique sur `lastname` puis sur `firstname` en cas d'égalité), par exemple pour pouvoir exécuter le code suivant :

```java
    TreeSet<Person> group= new TreeSet<Person>();
    group.add(new Person("Bernard","H"));
    group.add(new Person("Jules", "L"));
    System.out.println(group);

```

Quel est le message d'erreur à l'exécution ?


<a id="org0d1ea87"></a>

## Implémentation de l'interface Comparable

Implémenter l'interface Comparable [Comparable](https://docs.oracle.com/javase/10/docs/api/java/lang/Comparable.html) avec une méthode `public int compareTo(Object o)`.


<a id="org732fcf4"></a>

## Implémentation de l'interface Comparable<Person>

Implémenter l'interface [Comparable<Person>](https://docs.oracle.com/javase/10/docs/api/java/lang/Comparable.html). Quels sont les avantages par rapport à l'implémentation précédente ?
