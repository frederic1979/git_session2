- [Principe](#org0af3f71)
- [JPA et Hibernate](#orgea3180c)
- [Mise en œuvre](#org95054cb)
  - [Dépendances](#org39b5d1a)
  - [Configuration XML](#orgc79688a)
  - [Annotations](#org85ed308)
- [Utilisation](#org33f0fd1)
  - [Construction d'un EntityManager](#org5aef88d)
  - [Utilisation d'EntityManager](#org374a970)
    - [Création](#org2ca1563)
  - [Lecture](#org81dd4fb)
  - [Mise à jour](#org25c2319)
  - [Suppression](#orgb09bc17)
- [Pratique](#orged7cbca)
- [Associations](#orgbcca5dc)
  - [1-N, N-1](#orgda0bc05)
  - [N-N](#org29ad975)
- [Data Access Objects](#orgca40791)
- [Java Persistence Query Language](#org05f53e2)
  - [Paramétrage](#org5455380)
  - [Typage](#orga7519c4)
  - [Définition statique](#org14e50fb)
- [Mise en œuvre](#orgef1e6a3)



<a id="org0af3f71"></a>

# Principe

Lorsque l'on implémente un CRUD à partir de JDBC, l'implémentation des DAO est extrêmement répétitive car toutes les entités doivent permettre les même fonctionnalités de base :

-   création de nouvelle entités destinées à être enregistrée dans la table associée à la classe
-   construction d'objets partir des lignes de la table associée à la classe
-   mise à jour des lignes de la table pour prendre en compte les modifications des objets lorsque les attributs de ceux-ci ont été modifiés
-   suppression des lignes correspondant à des objets que l'on veut supprimer.

Les principales différences entre deux classes entités, sont :

-   le nom de la table associée à la classe
-   les noms et types des colonnes associées à chaque attributs

Dans le cas un peu plus complexe de l'implémentation de relations entre entités, on doit aussi prendre en compte le type de relation (1-1, 1-plusieurs, plusieurs-1, plusieurs-plusieurs, et si elles sont unidirectionnelles ou bidirectionnelles) et identifier la table d'association éventuelle ainsi que décider si le chargement des entités associées doit être [paresseux](https://fr.wikipedia.org/wiki/%C3%89valuation_paresseuse) ([lazy](https://en.wikipedia.org/wiki/Lazy_evaluation)) ou non.

Si l'on pouvait *déclarer* ces *paramètres* l'implémentation de la correspondance entre les classes entités et les tables pourrait être automatisée. Il sera ainsi possible de manipuler les données de la base en désignant les classes et attributs au lieu des tables et colonnes correspondantes grâce à un *Domain Specific Language* adapté : [Java Persistence Query Language](https://www.thoughts-on-java.org/jpql/) (*JPQL*).

Le fait d'utiliser JPQL plutôt que SQL nous permettra aussi, dans un deuxième temps, de factoriser une partie des implémentations de nos *DAO*.


<a id="orgea3180c"></a>

# JPA et Hibernate

La correspondance entre les tables des Systèmes de Bases de Données Relationnels et les classes de la Programmation Orientée Objet permet de définir un *Mapping Objet-Relationnel*. En Java, [JPA](https://fr.wikipedia.org/wiki/Java_Persistence_API) (Java Persistence API) est la spécification standard et [Hibernate](https://fr.wikipedia.org/wiki/Hibernate) en est l'implémentation la plus populaire (même si [EclipseLink](https://www.eclipse.org/eclipselink/) est l'implémentation de référence). On a le même rapport entre spécification et implémentation qu'entre des *interfaces* et les classes implémentant ces interface (ces classes peuvent aussi implémenter plus que ce qui est spécifié par les interfaces).

Afin de ne pas dépendre d'une implémentation spécifique, on pourra vouloir se restreindre à n'utiliser que ce qui est spécifié par *JPA* même si l'on utilise *Hibernate*.

*JPA* constitue **encore** une couche d'abstraction. En tant que telle, elle ne sera pas vraiment utile pour de petits projets n'ayant pas besoin d'évoluer. Le couplage avec le typage statique de Java procède des mêmes avantages et inconvénients.


<a id="org95054cb"></a>

# Mise en œuvre


<a id="org39b5d1a"></a>

## Dépendances

On peut utiliser *JPA* et *Hibernate* dans le cadre de *frameworks* (e.g. [Spring](https://spring.io/guides/gs/accessing-data-jpa/) boot, voire [JHipster](https://www.jhipster.tech/creating-an-entity/)), mais dans un premier temps, on utilisera seulement/directement *JPA* et *Hibernate* dans un projet *Maven*.

```nxml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.8</version>
</dependency>

<dependency>
    <groupId>org.eclipse.persistence</groupId>
    <artifactId>javax.persistence</artifactId>
    <version>2.2.1</version>
</dependency>
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-core</artifactId>
    <version>5.4.9.Final</version>
</dependency>

```


<a id="orgc79688a"></a>

## Configuration XML

Dans la structure standard d'un projet *Maven*, on ajoutera un répertoire `META-INF` dans le répertoire `src/main/java` et dans ce répertoire un fichier `persistence.xml` :

```XML
<persistence xmlns="http://xmlns.jcp.org/xml/ns/persistence" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence
             http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd"
  version="2.1">
<persistence-unit name="demo-jpa-1" transaction-type="RESOURCE_LOCAL">
    <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>
		<class>co.simplon.patrimoine.model.City</class>
		<class>co.simplon.patrimoine.model.Monument</class>
    <properties>
        <property name="javax.persistence.jdbc.driver" value="org.postgresql.Driver" />
 
        <property name="javax.persistence.jdbc.url" value="jdbc:postgresql://localhost/postgres" /> <!-- !!! -->
        <property name="javax.persistence.jdbc.user" value="****" /> <!-- !!! --> 
        <property name="javax.persistence.jdbc.password" value="****" /> <!-- !!! -->
        
        <property name="hibernate.dialect" value="org.hibernate.dialect.PostgreSQL95Dialect"/> <!-- DB Dialect -->
        <property name="hibernate.hbm2ddl.auto" value="update" /> <!-- create / create-drop / update -->    
        <property name="hibernate.show_sql" value="true" /> <!-- Show SQL in console -->
        <property name="hibernate.format_sql" value="true" /> <!-- Show SQL formatted -->
    </properties>

</persistence-unit>
</persistence>
```

-   **Exercice:** Que penser des propriétés `javax.persistence.jdbc.url` et surtout `javax.persistence.jdbc.user` voire `javax.persistence.jdbc.password` ? Que proposez-vous ?

Les autres propriétés de configuration de JPA pourraient elles aussi être exprimée en XML, [dans un fichier orm.xml](https://dzone.com/articles/persisting-entity-classes). Mais comme elles sont liées aux classes entités, on préférera les exprimer sous la forme d'*annotations*.


<a id="org85ed308"></a>

## Annotations

Dans les classes `co.simplon.patrimoine.model.City` et `co.simplon.patrimoine.model.Monument`, on utilisera les annotations suivantes :

-   sur la classe :
    -   [javax.persistence.Entity](https://docs.oracle.com/javaee/6/api/javax/persistence/Entity.html)
    -   [javax.persistence.Table](https://docs.oracle.com/javaee/7/api/javax/persistence/Table.html)
-   sur les attributs :
    -   [javax.persistence.Id](https://docs.oracle.com/javaee/7/api/javax/persistence/Id.html) pour l'attribut correspondant à la clé primaire
    -   [javax.persistence.GeneratedValue](https://docs.oracle.com/javaee/7/api/index.html?javax/persistence/GeneratedValue.html) toujours pour la clé primaire. Avec une valeur de [strategy](https://docs.oracle.com/javaee/7/api/javax/persistence/GeneratedValue.html#strategy--) à [GenerationType.SEQUENCE](https://docs.oracle.com/javaee/7/api/javax/persistence/GenerationType.html#SEQUENCE), dans le cas d'une clé primaire de type `SERIAL` sous postgresql, [notamment pour des raisons de performance](https://www.thoughts-on-java.org/hibernate-postgresql-5-things-need-know/).
    -   [javax.persistence.Column](https://docs.oracle.com/javaee/7/api/javax/persistence/Column.html) pour chacun des attributs.

Sur les classes suivantes :

```java
  public class City {
      private Long id;
      private String name;
      private Double latitude;
      private Double longitude;

      public City() {
      }
      public City(String name, double latitude, double longitude) {
	  this(null, name, latitude, longitude);
      }
      public City(Long id, String name, double latitude, double longitude) {
	  this.id= id;
	  this.name= name;
	  this.latitude= latitude;
	  this.longitude= longitude;
      }
      public Long getId() {
	  return id;
      }

      public void setId(Long id) {
	  this.id = id;
      }

      public String getName() {
	  return name;
      }

      public void setName(String nom) {
	  this.name = nom;
      }

      public Double getLongitude() {
	  return this.longitude;
      }

      public void setLongitude(Double longitude) {
	  this.longitude = longitude;
      }

      public Double getLatitude() {
	  return this.latitude;
      }

      public void setLatitude(Double latitude) {
	  this.latitude = latitude;
      }

      @Override
      public String toString() {
	  return "City [id=" + id + ", name=" + name + ", latitude=" + latitude
	      + ", longitude=" + longitude + "]";
      }
      // TODO hashCode() & equals()
  }

```

Cette classe doit être liée à une table nommée `CITIES` avec des colonnes :

-   **ID:** clé primaire de type `SERIAL`
-   **NAME:** 

-   **LATITUDE:** 

-   **LONGITUDE:** 

-   **Exercice:** Indiquer que la valeur d'une colonne ne doit pas être `NULL` et qu'une chaîne de caractères doit avoir une taille limitée à 255 caractères ?


<a id="org33f0fd1"></a>

# Utilisation


<a id="org5aef88d"></a>

## Construction d'un EntityManager

Au lieu d'utiliser directement des objets de type [java.sql.Connection](https://docs.oracle.com/javase/7/docs/api/java/sql/Connection.html), on interagit désormais avec la base de données à travers des objets de type [javax.persistence.EntityManager](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html). Pour construire un tel objet en prenant en compte les propriétés définies dans le fichier `persistence.xml`, on utilise une [javax.persistence.EntityManagerFactory](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManagerFactory.html). Lorsque l'on récupère cet objet *factory*, on indique le nom de la `persistence-unit` définie dans le fichier `persistence.xml` ainsi qu'une éventuelle table d'association ([Map](https://docs.oracle.com/javase/9/docs/api/java/util/Map.html))qui permet de redéfinir certaines valeurs à l'exécution, par exemple les informations confidentielles :

```java
String persistenceUnitName= "demo-jpa-1"; // defined in persistence.xml
Map<String, String> env = System.getenv();
Map<String, Object> configOverrides = new HashMap<String, Object>();
for (String envName : env.keySet()) {
  if (envName.contains("DB_USER")) {
    configOverrides.put("javax.persistence.jdbc.user", env.get(envName));
  }
  if (envName.contains("DB_PASS")) {
    configOverrides.put("javax.persistence.jdbc.password", env.get(envName));
  }
  if (envName.contains("DB_URL")) {
    configOverrides.put("javax.persistence.jdbc.url", env.get(envName));    
  }
}
EntityManagerFactory entityManagerFactory = Persistence.createEntityManagerFactory(persistenceUnitName
                                            ,configOverrides);
```

(Si besoin, [ajuster la configuration d'Eclipse pour qu'il reconnaisse le contenu du fichier persistence.xml](https://stackoverflow.com/a/13854580)).

**Attention !** Comme l' `EntityManagerFactory` gère la connection, il doit être fermé par un appel à `close()`. Heureusement, cette classe implément l'interface [AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html).


<a id="org374a970"></a>

## Utilisation d'EntityManager

On peut utiliser l'objet de type `EntityManager` pour insérer un nouvel objet dans la table avec un appel à la méthode [persist](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html#persist-java.lang.Object-).

-   **Exercice:** vérifier la valeur de l'attribut `id` avant et après l'appel à `persist`.


<a id="org2ca1563"></a>

### Création

On peut créer une class `Main` avec l' `EntityManagerFactory` en attribut (ici `factory`) <sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup> :

```java
  public City createCity() {
      EntityManager em= factory.createEntityManager();
      City city= new City("Atlantis", 0, 0.5);
      city= create(em, city);
      em.close();
      return city;
  }
  public City create(EntityManager em, City city) {
      em.getTransaction().begin();
      em.persist(city);
      em.getTransaction().commit();
      return city;
  }
```

Une fois l'instance de la classe entité passée en argument à `persist`, celle-ci devient gérée (*managed*) par l'`EntityManager`. Ensuite, toutes modifications des attributs de l'objet effectuée avant l'appel à `commit` de l'`EntityManager` sera automatiquement répercutée :

```java
  public City createCityAndUpdate() {
	  EntityManager em= factory.createEntityManager();
	  City city= new City("Paris", 0, 0.5);
	  em.getTransaction().begin();
	  em.persist(city);
	  city.setLatitude(1000.);
	  em.getTransaction().commit();// MAGIC HAPPENS HERE !
	  em.close();
	  return city;
  }
```

-   **Exercice:** Observer le résultat de la gestion automatique dans la base de donnée.


<a id="org81dd4fb"></a>

## Lecture

On peut lire directement une entité à partir de l'`EntityManager` à partir de la valeur de la clé primaire :

```java
  public City readCity() {
      EntityManager em= factory.createEntityManager();
      City city= readCity(em, 4L);
      em.close();
      return city;
  }
  public City readCity(EntityManager em, Long id) {
      return em.find(City.class, id);
  }
```

-   **Exercice:** Que se passe-t-il si l'on change un attribut de l'objet lu ? Et si l'on effectue une transaction ensuite ?


<a id="org25c2319"></a>

## Mise à jour

Lorsqu'on s'attend à ce qu'un objet soit déjà présent dans la base (l'attribut correspondant à la clé primaire doit donc avoir une valeur), et que l'on veut, le cas échéant récupérer une référence sur un objet géré par la base sans confier la gestion de l'objet passé en argument à l'`EntityManager`, on utilise `merge` plutôt que `persist`.

```java
  public City updateCity() {
      return update(new City(4L,"PaRiS", -1., -2.));
  }
  public City update(City city) {
      EntityManager em= factory.createEntityManager();
      em.getTransaction().begin();
      city = em.merge(city);
      em.getTransaction().commit();
      return city;
  }
```

-   **Exercice:** Constater si l'instance retournée par `merge` est gérée (*managed*).


<a id="orgb09bc17"></a>

## Suppression

On peut vouloir supprimer un objet selon deux cas de figures :

-   à partir de la valeur de la clé primaire
-   à partir d'une instance de la classe entité

-   **Exercice:** Implémenter les deux cas de figure à l'aide de la méthode [remove](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html#remove-java.lang.Object-) de l'`EntityManager`. Dans le deuxième cas de figure, prendre en compte que l'instance passé en argument doit être *gérée* par l'`EntityManager`.


<a id="orged7cbca"></a>

# Pratique

Implémenter les mêmes fonctionnalités pour une classe `Monument` :

```java
  public class Monument {
      private Long id;
      private String name;

      /* TODO
	  private City city;
      */
      public Monument(String name) {
	  super();
	  this.name = name;
      }
      public Monument() {
      }
      public Long getId() {
	  return this.id;
      }
      public void setId(Long id) {
	  this.id = id;
      }
      public String getName() {
	  return this.name;
      }
      public void setName(String name) {
	  this.name = name;
      }
      /*
      public City getCity() {
	  return city;
      }
    
      public void setCity(City city) {
	  this.city = city;
      }
      */
      @Override
      public String toString() {
	  return "Monument [id=" + id + ", name=" + name
	      + ", city=" /*+ city */+ "]";
      }
  }
```


<a id="orgbcca5dc"></a>

# Associations

On peut [utiliser JPA pour modéliser tous types d'associations](https://thoughts-on-java.org/ultimate-guide-association-mappings-jpa-hibernate/).


<a id="orgda0bc05"></a>

## 1-N, N-1

On va vouloir modéliser une association entre :

-   un monument et une ville
-   une ville et des monuments

Au niveau des entités, on peut ajouter des attributs (et accesseurs qui vont avec) :

-   dans la classe `Monument` :
    
    ```java
      private City city;
    ```
-   dans la classe `City` :
    
    ```java
      private List<Monument> monuments = new ArrayList<Monument>();
    ```

Remarque : On peut [utiliser d'autres types de Collection que List](https://www.thoughts-on-java.org/association-mappings-bag-list-set/).

Au niveau de la base de données, il suffirait d'avoir une colonne `city` (ou `fk_city` suivant la convention de nommage) comme clé étrangère.

On peut indiquer cela avec les annotations suivantes :

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "city")
private City city;
```

et

```java
@OneToMany(mappedBy = "city")
private List<Monument> monuments = new ArrayList<Monument>();
```

-   **Exercices:** [Quel est l'effet](https://www.thoughts-on-java.org/entity-mappings-introduction-jpa-fetchtypes/) de `fetch = FetchType.Lazy` ?

Quel seraient les effets du codes suivant ?

```java
@OneToMany(mappedBy = "city", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
private Set<Monument> monuments;
```

-   **Exercice:** Modifier la méthode `createMonument` du programme principal pour créer un monument qui soit rattaché à une ville.


<a id="org29ad975"></a>

## N-N

On va ajouter une classe `User` qui permettra de modéliser des utilisateurs de notre application. Chaque utilisateur peut avoir visité plusieurs monuments et chaque monument peut avoir été visité par plusieurs utilisateurs.

```java

import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinTable;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name = "USERS")
public class User {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "ID")
	private Long id;

	@Column(name = "NAME", nullable = false, length = 100)
	private String name;
	
	@ManyToMany
        @JoinTable(name= "USER_MONUMENT",
                   joinColumns = {@JoinColumn(name = "FK_USER", referencedColumnName= "ID" ) },
                   inverseJoinColumns = { @JoinColumn(name = "FK_MONUMENT", referencedColumnName= "ID") })
        private Set<Monument> monuments = new HashSet<Monument>();
	
	public User() {
	}
	public User(String name) {
		this.name= name;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name= name;
	}
	public void addMonument(Monument m){
		monuments.add(m);
		m.getUsers().add(this);
	}
	public Set<Monument> getMonuments(){
		return monuments;
	}
	public void setMonuments(Set<Monument> monuments) {
		this.monuments= monuments;
	}
	public String toString() {
		return "User :{ id= "+id+"\n name= "+name+"\n nb momunents"+ monuments.size()+"\n}";
	}
	
}
```

Et en ajoutant dans la classe `Monument` l'attribut annoté suivant (et ses accesseurs) :

```java
  @ManyToMany(mappedBy="monuments")
  private Set<User> users = new HashSet<User>();
```

-   **Exercice:** Implémenter un méthode `createUser` .


<a id="orgca40791"></a>

# Data Access Objects

Implémenter les DAOs selon les interfaces suivantes :

```java
  public interface MonumentDao {
      Monument createMonument(Monument monument);
      Monument getMonumentById(Long id);
      Monument updateMonument(Monument monument);
      void deleteMonumentById(Long id);
  }
```

```java
  public interface CityDao {
      City createCity(City city);
      City getCityById(Long id);
      City updateCity(City city);
      void deleteCityById(Long id);
  }
```

```java
  public interface UserDao {
      User createUser(User user);
      User getUserById(Long id);
      User updateUser(User user);
      void deleteUserById(Long id);
  }
```

-   **Exercices:** -   Factoriser les interfaces avec une interface *générique*.
    -   Factoriser les implémentations avec une classe de base *générique*.

Bien sûr, les méthodes `find`, `persist`, `merge` et `remove` ne suffisent pas à interagir avec la base de données. [Il est possible d'utiliser l'EntityManager pour effectuer des requêtes SQL](https://www.thoughts-on-java.org/jpa-native-queries/) avec la méthode [createNativeQuery](http://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html#createNativeQuery-java.lang.String-). Cependant, on pourra tirer un parti plus avantageux des correspondances classes / tables, attributs / colonnes, objets / lignes en écrivant des requêtes manipulant des classes, attributs et objets plutôt que des tables, colonnes et tuples avec un nouveau *DSL* (*Domain Specific Language*).


<a id="org05f53e2"></a>

# Java Persistence Query Language

[JPQL reprend exactement les principes de SQL](https://www.thoughts-on-java.org/jpql/) et l'on peut passer une `String` de code `JPQL` en argument à la méthode [createQuery](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html#createQuery-java.lang.String-) de l'objet `EntityManager` de ma même façon qu'on utilisait par exemple la méthode [execute](https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#execute(java.lang.String)) d'un objet `java.sql.Statement`. Ainsi, pour lister tous les monuments en les triant dans l'ordre alphabétique, le code JPQL sera :

```java
" SELECT m FROM Monument m ORDER BY m.nom "
```


<a id="org5455380"></a>

## Paramétrage

Il est bien sûr aussi possible de paramétrer les requêtes *JQPL*. On peut utiliser deux types de paramètres :

-   **positionnels:** Ils sont indiqué dans la requête *JPQL* sous la forme `?1`, `?2` …
    
    ```java
    		  "SELECT c FROM City AS c WHERE c.name=?1"
    ```
-   **nommés:** Ils sont indiqués dans la requête *JPQL* sous la forme `:nom` :
    
    ```java
    	    "SELECT c FROM City AS c WHERE c.name=:nameParam"
    ```

Un appel à la méthode [setParameter](https://docs.oracle.com/javaee/7/api/javax/persistence/Query.html#setParameter-int-java.lang.Object-) prenant un `int` en premier argument ou à [setParameter](https://docs.oracle.com/javaee/7/api/javax/persistence/Query.html#setParameter-java.lang.String-java.lang.Object-) prenant une chaîne de caractères (le nom **sans** le préfixe ':') en premier argument permet d'assigner une valeur à un paramètre avant d'exécuter la requête.

-   **Exercice:** Utiliser des requêtes JPQL, notamment en explorant les [opérateurs sur les chaînes de caractères](https://www.objectdb.com/java/jpa/query/jpql/string#LIKE___String_Pattern_Matching_with_Wildcards_) plutôt qu'une simple égalité.


<a id="orga7519c4"></a>

## Typage

Plutôt que de récupérer des références de type `Object`, on préférera récupérer directement selon leur vrai type les instances de nos entités. On peut utiliser pour cela des objets de type [TypedQuery](https://docs.oracle.com/javaee/7/api/javax/persistence/TypedQuery.html) :

```java
TypedQuery<City> query = em.createQuery("SELECT c FROM City AS c WHERE c.name=:nameParam"
                                        , City.class);
query.setParameter("nameParam", "Paris");
for (City c : query.getResultList()) {
    System.out.println(c);
}
```


<a id="org14e50fb"></a>

## Définition statique

Grâce au paramétrage de requêtes, la plupart des requêtes peuvent être fixées à la compilation. Cela permet d'utiliser des *requêtes nommées* (*NamedQueries*) définies par des annotations. Par exemple :

```java
@NamedQueries({
		@NamedQuery(name = "City.findAll", query = " SELECT c FROM City c ORDER BY c.name "),
		@NamedQuery(name = "City.deleteById", query = " DELETE FROM City c WHERE c.id = :id") })
```

Il est d'usage de situer ces annotations au niveau de la classe Entité qu'elles concernent (par exemple après les annotations `@Entity` et `@Table`). De même qu'il est d'usage d'utiliser le nom de la classe comme préfixe dans les noms des *requêtes nommées*.

On peut ensuite utiliser ces requêtes nommées de la façon suivante :

```java
  public List<City> findAll(int first, int size) {
      return entityManager.createNamedQuery("City.findAll", City.class)
	  .setFirstResult(first).setMaxResults(size).getResultList();
  }


```

-   **Exercices:** -   Implémenter des méthodes `findAll` avec des *requêtes nommées* pour les classes `Monument` et `User`.
    -   Implémenter des méthodes `deleteById` avec des *requêtes nommées* pour les classes `City`, `Monument` et `User`.


<a id="orgef1e6a3"></a>

# Mise en œuvre

Implémenter un CRUD en utilisant *JPA* ! Remarquer qu'on a les mêmes problèmes de durées de vie/partage pour les objets de type `EntityManager` que pour les objets de type `Connection`.

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Ici, on a utilisé un attribut
d'instance et des méthodes d'instance et `Main.main(String[] args)` devrait donc instancier la classe
`Main`. L'intérêt par rapport à un attribut
`static` est que l'on peut ainsi gérer la
fermeture de la factory en faisant cette instanciation dans un *try
with resources*.
