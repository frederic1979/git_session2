- [Modélisation](#org9d548e7)
- [Implémentation](#org8065b7b)
  - [Fonctionnalités de base](#org863c430)
    - [equals](#org0d82793)
    - [hashCode](#orge0e0966)
  - [Fonctionnalités demandées](#orga315f7c)
    - [distance d'une commune à un point](#orgf60a025)
    - [distance d'une commune à une autre](#org749e156)
    - [commune la plus proche](#org2a37e45)
    - [communes dans un rayon par rapport à un point](#orgb57efad)
    - [Communes dans un rayon par rapport à un ensemble de points](#org1b452cb)
  - [Lecture des données](#org84921f2)



<a id="org9d548e7"></a>

# Modélisation

La principale question est de décider comment on va représenter les coordonnées géographiques. Il y a trois possibilités (en plus du fait de choisir un type `float` ou src\_java[:exports code]{double] pour les latitudes et longitudes) :

-   les représenter juste par deux nombres distincts
-   les regrouper :
    -   dans un tableau de deux cases
    -   dans une classe dédiée (par exemple `GeoCoords`).

Il s'agit de différents compromis entre facilité, simplicité et performance. Les problèmes posés par le fait de ne pas regrouper les coordonnées sont :

-   il faudra faire attention à l'ordre dans lequel on passe les paramètres à chaque fois (même si l'IDE peut nous aider)
-   pour la méthode qui implémentera l'opération «trouver les communes qui sont simultanément dans un rayon donnée d'un ensemble de points quelconques repérés par leur latitude et longitude.», il ne sera pas commode de passer ces points.

Un tableau de deux cases peut résoudre le problème, mais le compilateur ne pourra pas vérifier que le tableau fait effectivement deux cases. **ATTENTION !** Si l'on utilise un tableau comme attribut de notre classe `City`, il faut se poser la question de l'égalité et du hashage de tableaux (utiliser [Arrays.equals](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#equals-double:A-double:A-) et non le `equals` qui est [celui de Object](https://docs.oracle.com/javase/9/docs/api/java/lang/Object.html#equals-java.lang.Object-), et [Arrays.hashCode](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#hashCode-double:A-) et non le `hashCode` qui est [celui de Object](https://docs.oracle.com/javase/9/docs/api/java/lang/Object.html#hashCode--)).

On peut aussi se demander si l'on a besoin d'une classe pour modéliser les ou les ensembles de communes. À priori, cela ne semble pas nécessaire.


<a id="org8065b7b"></a>

# Implémentation


<a id="org863c430"></a>

## Fonctionnalités de base


<a id="org0d82793"></a>

### equals


<a id="orge0e0966"></a>

### hashCode


<a id="orga315f7c"></a>

## Fonctionnalités demandées

Certaines opérations qui se réfèrent à une commune en particulier, on les implémentera donc sous la forme de méthodes d'instance. Pour les autres, on utilisera des méthodes de classe. Pour les ensembles de communes acceptés en argument et retournés, on doit se demander le type à utiliser. Pour le type acceptés, on voudra utiliser l'interface la plus générique : [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html). Pour les types retournés, on doit décider si l'on veut supprimer les doublons et/ou si l'on veut pouvoir faire efficacement des intersections. Dans ces cas, on utilisera des [Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html) (par exemple [HashSet](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html) si l'on a pas d'ordre à gérer). Sinon, on pourra utiliser des [ArrayList](https://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html) qu'on pourra retourner en tant que [List](https://docs.oracle.com/javase/7/docs/api/java/util/List.html), voire [Collection](https://docs.oracle.com/javase/7/docs/api/java/util/Collection.html). Retourner une [List](https://docs.oracle.com/javase/7/docs/api/java/util/List.html) permet de faire plus de choses, mais


<a id="orgf60a025"></a>

### distance d'une commune à un point

```java
    public double distanceTo(double latitude, double longitude){
        double R= 6371e3;
        double phi1=Math.toRadians(this.latitude);
        double phi2=Math.toRadians(latitude);
        double deltaPhi=Math.toRadians(latitude- this.latitude);
        double deltaLambda= Math.toRadians(longitude- this.longitude);
        double a= Math.sin(deltaPhi/2) * Math.sin(deltaPhi/2) +
            Math.cos(phi1) * Math.cos(phi2) * Math.sin(deltaLambda/2) * Math.sin(deltaLambda/2);
        double c= 2* Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        return R * c;
    }
```


<a id="org749e156"></a>

### distance d'une commune à une autre

```java
    public double distanceTo(City other){
        return distanceTo(other.latitude, other.longitude);
    }
```


<a id="org2a37e45"></a>

### commune la plus proche

Il faut juste faire attention à ne pas retourner l'instance elle-même qui est évidemment la plus proche à elle-même. Les questions à se poser sont :

-   quel est le type à utiliser pour l'ensemble des communes reçues en argument ?
-   est-ce qu'on veut retourner une instance qui serait égale à l'instance de référence, si elle est présente dans l'ensemble reçu en argument.
-   que retourner s'il n'y a pas de communes la plus proche ! (Ce qui arrive si et seulement si l'ensemble de communes est vide ou ne contient que des instances égales à la commune de référence).

```java
public City closestCity(Collection<City> cities){
    City res = null;
    double minDist = Double.MAX_VALUE;
    for(City city : cities){
	if( !equals(city) ){
	    double d = distanceTo(city);
	    if (d < minDist){
		minDist = d;
		res = city;
	    }
	}
    }
    return res;
}
```


<a id="orgb57efad"></a>

### communes dans un rayon par rapport à un point

Comme on retourne

```java
public static List<City> inRadius(double radius, double latitude, double longitude, Collection<City> cities){
    List<City> res = new ArrayList<City>();
    for(City city : cities){
	if(city.distanceTo(latitude, longitude) <= radius){
	    res.add(city);
	}
    }
    return res;
}
```


<a id="org1b452cb"></a>

### Communes dans un rayon par rapport à un ensemble de points

Si l'on a pas utilisé de classe dédiée (i.e. `GeoCoords`) ou de tableau pour regrouper les latitude et longitude, on doit se poser la question du type utilisé pour recevoir les coordonnées en argument. On ne voudra pas avoir deux tableaux `double[] latitudes` et `double[] longitudes`. Il faut aussi décider de la valeur retournée lorsque l'ensemble de points est vide. On pourrait aussi bien décider de retourner une liste vide qu'une liste contenant toutes les communes passées en argument.

```java
public static List<City> inRadius(double radius, Collection<double[]> points, Collection<City> cities){
    List<City> res= new ArrayList<City>(cities);
    for(double[] p : points){
	res= inRadius(radius, p[0], p[1], res);
    }
    return res;
}	
```


<a id="org84921f2"></a>

## Lecture des données

```java
public static List<City> read(String citiesURL) throws IOException {
    List<City> res = new ArrayList<City>();
    URL url = new URL(citiesURL);
    try(BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()))){
	br.readLine(); // on passe la ligne d'entête
	for(String line = br.readLine(); line != null; line = br.readLine()){
	    String[] data = line.split(";");
	    if(data.length == 3){
		try{
		    res.add(new City(data[0], Double.parseDouble(data[1]), Double.parseDouble(data[2])));
		}catch(Exception e){
		    System.err.println("Erreur à la lecture de la ligne:\n"+line);
		    System.err.println(e);
		}
	    }
	}
    }
}
```
