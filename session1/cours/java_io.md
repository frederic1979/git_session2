- [Utilisation de la console](#orgf8095a2)
  - [Écriture dans la console](#orga0625e1)
  - [Lecture dans la console](#org13afbfa)
- [Exceptions](#org45249f3)
- [Utilisation de fichiers](#orgd53004f)
  - [Exceptions vérifiées](#org8065b91)
  - [Chemin absolu ou relatif, répertoire courant](#org543a4dd)
  - [Écriture dans un fichier](#orgc642419)
  - [Lecture depuis un fichier](#org882c51a)
- [<a id="orge248a59"></a>Gestion des Exceptions](#org7c16ce1)
  - [try / catch / finally](#org11adba5)
  - [try avec ressources](#org4d6eb30)



<a id="orgf8095a2"></a>

# Utilisation de la console

Lorsqu'on exécute un programme en mode console, par exemple dans un terminal, mais les IDE ont aussi une fenêtre "Console", on peut écrire du texte à l'écran et lire du texte à saisi au clavier.


<a id="orga0625e1"></a>

## Écriture dans la console

On a déjà vu comment écrire des données sur l'écran d'une console : avec les *méthodes* [print](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#print-java.lang.String-) et [println](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#println-java.lang.String-) appelées sur les *objets* [System.out](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#out) ou [System.err](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#err).

On parle de *méthodes* car contrairement aux fonctions qu'on a écrites, celles-ci sont appelées sur un *objet* : `nomDeLObjet.nomDeLaMethode(premierArg, secondArg)`. Les méthodes qu'on peut appeler sur un *objet* sont définis par la *classe* dont il est une *instance* (ce qui veut dire que la classe est le type de l'objet). On a déjà vu par exemple des instances de la classe [String](https://docs.oracle.com/javase/9/docs/api/java/lang/String.html).

[System.out](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#out) écrit sur la [sortie standard](https://fr.wikipedia.org/wiki/Flux_standard#Sortie_standard) qui sert aux messages lors du fonctionnement normal du programme et [System.err](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#err) écrit sur la [sortie d'erreurs](https://fr.wikipedia.org/wiki/Flux_standard#Erreur_standard) qui sert aux messages d'erreur. Par défaut, les deux sont affichés à l'écran mais on peut les rediriger indépendamment vers des fichiers. Sous IntelliJ, les deux sont affichés sur la console, mais les messages sur la sortie d'erreur affichés en rouge.

En consultant la documentation de la classe dans laquelle [print](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#print-java.lang.String-) et [println](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#println-java.lang.String-) sont définies, on constate que ces méthodes sont *surchargées* et qu'il y a des implémentations pour tous les types primitifs.

Par ailleurs, il est possible de passer des tableaux en arguments.

-   **Exercice:** Constater et comprendre le résultat d'un appel de [print](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#print-java.lang.String-) en passant en argument des tableaux de différents types.


<a id="org13afbfa"></a>

## Lecture dans la console

Par défaut, les lecture dans la console correspondent aux saisies au clavier, qui sont envoyées lors de l'appui sur la touche ⏎ (ou ↵). [System.in](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#in) correspond à l'[entrée standard](https://fr.wikipedia.org/wiki/Flux_standard#Entr%C3%A9e_standard) de la console qui peut être utilisée comme source brute de données sous forme d'octets.

En pratique, on ne voudra généralement pas lire directement des octets en tant que tel, mais lire des donnés des types de Java (e.g. `int`,`long`,`float`,`double`,`String`). Pour cela, la bibliothèque standard met à disposition la classe [java.util.Scanner](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) utilisée comme suit :

```java
 1  /*
 2   La directive import suivante permet ensuite d'écrire Scanner sans
 3   avoir à écrire java.util.Scanner
 4  */
 5  import java.util.Scanner;
 6  
 7  public class ScannerDemo {
 8      public static void main(String[] args){
 9  	Scanner sc = new Scanner(System.in); // lecture depuis l'entrée standard (clavier)
10  	System.out.println("Saisissez un entier:");
11  	int i = sc.nextInt();
12  	System.out.println("Vous avez saisi: "+ i);
13  	System.out.println("Saisissez un double (penser à la localisation!):");
14  	double d = sc.nextDouble(); // /!\ Si l'ordinateur est configuré en fr_FR, le séparateur décimal attendu est une virgule !
15  	System.out.println("Vous avez saisi: "+ d);
16  	System.out.println("Saisissez une ligne de caractères");
17  	sc.nextLine(); // /!\ le dernier appel à nextDouble() n'avait pas consommé la fin de ligne !
18  	String line = sc.nextLine();
19  	System.out.println("Vous avez saisi: "+ line);
20      }
21  }
```

Il faut donc :

1.  importer la classe `java.util.Scanner`
2.  instancier un objet de cette classe en passant en argument du constructeur l'objet qui représente l'entrée standard de la console : `Scanner sc = new Scanner(System.in)` (Bien évidemment, on donne le nom qu'on veut à la variable utilisée pour stocker la référence de l'objet créé.
3.  utiliser ensuite la méthode correspondant au type de donnée à lire

-   **Exercices:**  
    -   **Compréhension de code:** Pourquoi la localisation est-elle importante pour lire les types de nombres avec une partie décimale ?
    -   **Codage exploratoire:** Que se passe-t-il si l'on enlève la ligne `sc.nextLine();` ? Pourquoi ?
    -   **Tests:** Que se passe-t-il si l'on se rentre pas un nombre lorsqu'un nombre est attendu ?


<a id="org45249f3"></a>

# Exceptions

Lorsqu'on a effectué une saisie invalide, par exemple avec un chaîne de caractères ne représentant pas un nombre, avec le programme précédant, on obtient un message d'erreur dans la console :

<p class="verse">
Exception in thread "main" java.util.InputMismatchException<br />
&#xa0;at java.util.Scanner.throwFor(Scanner.java:864)<br />
&#xa0;at java.util.Scanner.next(Scanner.java:1485)<br />
&#xa0;at java.util.Scanner.nextInt(Scanner.java:2117)<br />
&#xa0;at java.util.Scanner.nextInt(Scanner.java:2076)<br />
&#xa0;at ScannerDemo.main(ScannerDemo.java:11)<br />
<br />
</p>

Il s'agit d'une [Exception](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html) qui indique une erreur à l'exécution, erreur dont la nature est indiquée par le type de l'exception, ici `java.util.InputMismatchException`, les lignes suivantes permettant de retracer l'origine de l'erreur (ici l'appel à la méthode `nextInt()` sur un objet de classe `java.util.Scanner` dans la fonction `main` de la classe `ScannerDemo` à la ligne `11` du fichier `ScannerDemo.java`.

-   **Exercices:**  
    -   **Compréhension:** Comprendre comment retrouver toutes les informations précédentes dans le message d'erreur (appelé *stack trace*).
    -   **Codage exploratoire:** Écrire des programmes pour déclencher les types d'erreurs suivantes (et comprendre les *stack traces*) :
        -   tentative de diviser par 0.
        -   tentative d'appeler une méthode sur une référence d'objet (de classe `String` ou `java.util.Scanner`) non initialisée.
        -   tentative d'accès à une case d'un tableau ou à la longueur d'un tableau par une référence non initialisé.
        -   tentative d'accès à une case d'un tableau correctement initialisé, mais avec un indice invalide (trop grand ou négatif).
        -   appel d'une fonction récursive sans condition d'arrêt.


<a id="orgd53004f"></a>

# Utilisation de fichiers


<a id="org8065b91"></a>

## Exceptions vérifiées

On vient de voir que certaines circonstances très fréquentes (un appel de fonction, une utilisation d'un objet ou l'accès à une case d'un tableau) pouvaient [déclencher des exceptions](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions#Java) (on dit *lancer* des exceptions car celles-ci remontent la pile d'appels de fonction, comme on peut le constater sur la *stack trace*). Bien sûr, on ne peut pas être paranoïaque au point de s'inquiéter à chaque fois qu'on utilise une référence, mais il y a des circonstances qui doivent a priori inciter à la prudence et à envisager des cas d'erreur. Par exemple à chaque fois qu'on utilise un fichier, il y a un risque d'erreur de lecture ou d'écriture (que le fichier ne soit pas accessible parce qu'il n'existe pas ou qu'on a pas les droits d'accès, où que le périphérique soit défaillant). Pour ces cas de figure, java dispose d'exceptions *contrôlées* ([Checked Exceptions](https://en.wikibooks.org/wiki/Java_Programming/Checked_Exceptions)) qui doivent être explicitement prises en compte. Lorsqu'on fait un appel à une méthode qui peut lancer une *checked exception* on doit obligatoirement faire l'une ou l'autre des choses suivantes :

-   [déclarer que la méthode qu'on est en train d'implémenter peut elle-même lancer (en fait, propager) une telle exception](https://docs.oracle.com/javase/tutorial/essential/exceptions/declaring.html) en utilisant le mot-clé `throws`
-   [gérer localement l'exception](https://docs.oracle.com/javase/tutorial/essential/exceptions/handling.html) en utilisant des blocs `try` / `catch` et éventuellement `finally`.

Seulement pour l'exposé des classes et méthodes mises en œuvre pour la lecture ou l'écriture dans un fichier, on se contentera d'ajouter `throws Exception` à la déclaration de la fonction du programme principal :

```java
public static void main(String[] args) throws Exception{
/* program that can throw (checked) exceptions for instance by calling
  methodes that throw checked exceptions */
}
```


<a id="org543a4dd"></a>

## Chemin absolu ou relatif, répertoire courant

Les fichiers et répertoires sont désignés par un chemin qui peut être :

-   **absolu:** le chemin commence alors par une barre oblique (*slash*) `/` sous Unix/MacOS qui indique la racine du système de fichier ou par l'identifiant d'un "lecteur"(*drive* `A:`, `B:`,…) sous Windows.
-   **relatif:** le chemin commence alors par `.` pour indiquer le répertoire courant (*working directory*) ou par `..` pour indiquer le répertoire parent <sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.

En pratique, le code d'un vrai programme ne devrait **jamais** contenir de chemin absolu vers un fichier de données dans un compte utilisateur car il ne pourrait alors fonctionner que sur la machine du développeur.

Lorsqu'on lance un programme depuis la console, le répertoire courant est celui dans lequel on exécute la commande pour lancer le programme. Lorsqu'on exécute un programme depuis un IDE, il faut savoir quel est le répertoire courant au lancement d'un programme. Il s'agit souvent du répertoire dans lequel est enregistré le projet mais on peut le modifier dans le configurations de lancement (de la même façon qu'on peut modifier les arguments passés au programme et récupérés dans l'argument de la fonction `public static void main(String[] args)`).


<a id="orgc642419"></a>

## Écriture dans un fichier

Il y a plusieurs façons d'écrire dans un fichier de texte, notamment en utilisant une instance spécifique de la classe [java.io.PrintStream](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html) à la place de [System.out](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#out) ou [System.err](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#err) (qui sont aussi des instances de cette classe). Il faut pour cela passer par un objet intermédiaire de la classe [java.io.FileOutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/FileOutputStream.html) :

```java
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.io.FileNotFoundException;

public class PrintStreamDemo {
    public static void main(String[] args) throws FileNotFoundException {
	PrintStream fileOut = new PrintStream(new FileOutputStream("textFile.txt"));
	fileOut.print("Hello ");
	fileOut.println("World !");
	fileOut.close();
    }
}
```

Vous pouvez ensuite utiliser l'instance de [java.io.PrintStream](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html) comme vous utiliseriez [System.out](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#out) ou [System.err](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#err), avec la seule différence qu'il faut appeler la méthode [close()](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#close--) qui fermera le fichier sous-jacent. En fait, il faudra s'assurer que cette fonction est bien appelée **dans tous les cas**, ce qui n'est pas évident dans le cas de lancement d'exceptions. Nous verrons comment faire en section [4](#orge248a59).


<a id="org882c51a"></a>

## Lecture depuis un fichier

Il y a plusieurs façons de lire le contenu d'un petit fichier de texte, mais on peut notamment utiliser une instance de la classe [java.io.File](https://docs.oracle.com/javase/8/docs/api/java/io/File.html) à la place de [System.in](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#in) :

```java
import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;

public class ScannerFromFileDemo {
    public static void main(String[] args) throws FileNotFoundException {
	Scanner sc = new Scanner(new File("inputFile.txt"));
	for(int i=0; sc.hasNextLine(); ++i){
	    System.out.println("["+i+"]:"+ sc.nextLine());
	}
	sc.close();
    }
}

```

De même que pour l'instance de l'instance de [java.io.PrintStream](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html), il faut désormais s'assurer que la méthode [close()](https://docs.oracle.com/javase/10/docs/api/java/util/Scanner.html#close()) est appelée.

-   **Exercice:** Modifier le programme ci-dessus pour qu'il lise les mêmes informations que le programme `ScannerDemo` et mettre le code de lecture dans une autre fonction appelée par java\_src[:exports code]{main}.


<a id="org7c16ce1"></a>

# <a id="orge248a59"></a>Gestion des Exceptions

En pratique, on ne peut évidemment pas se contenter de laisser les exceptions se propager. On va donc les [gérer localement](https://docs.oracle.com/javase/tutorial/essential/exceptions/handling.html) en utilisant des blocs `try` / `catch` et éventuellement `finally`.


<a id="org11adba5"></a>

## try / catch / finally

On doit commencer par déclarer le début d'un bloc `try` avant de faire l'opération qui peut lancer une exception contrôlée. Le bloc `try` doit non seulement contenir cette opération, mais toutes celles-ci en dépendent, par exemple tout le code qui utilise un objet dont la construction aurait pu déclencher une exception.

À la suite de ce bloc, on indique quelle exception on veut intercepter avec un bloc `catch`. bloc `catch` prend un argument dont le type est celui de l'exception à intercepter, ce qui permet d'utiliser cet argument ensuite dans le bloc.

On doit utiliser un bloc `finally` lorsqu'il y a du code qui doit être exécuté dans tous les cas :

-   pas d'exception ou exception interceptée
-   exception propagée

-   **Exercice:**  
    -   **Modification de code:** Modifier les programmes précédents pour que `main` ne laisse plus échapper d'exception mais affiche un message d'erreur. N'oubliez pas que l'appel à `.close()` doit être effectué **dans tous les cas**.
    
    -   **Ajout de fonctionalité:** Modifier les programmes précédents pour qu'en cas d'erreur, ils proposent de recommencer :
        -   en effectuant une autre saisie pour la lecture d'un nombre
        
        -   en saisissant un nom de fichier pour la lecture à partir d'un fichier (dans le cas d'une `FileNotFoundException`).

Pour aller plus loin, [une ressource indiquant notamment comment créer ses propres types d'exceptions](https://www.jmdoudoux.fr/java/dej/chap-exceptions.htm).


<a id="org4d6eb30"></a>

## try avec ressources

On a vu qu'il est fréquent d'avoir :

1.  la création d'un objet représentant une ressource,
2.  l'utilisation de cette ressource qui peut lancer <sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup> une exception,
3.  l'obligation d'appeler une méthode `close()` sur cet objet pour libérer la ressource.

La façon de gérer classiquement ce cas de figure obligeait à penser au bloc `finally` pour y effectuer l'appel à `close()`. La situation devient encore plus compliquée si l'appel à `close()` lui-même lançait une exception !

Pour gérer automatiquement tout cela, la version 7 de Java a apporté une nouvelle construction : le [try-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html).

-   **Exercice:** Réécrire les programmes en utilisant le [try-with-resources](https://www.jmdoudoux.fr/java/dej/chap-java7.htm#java7-5).

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> on peut remonter dans
l'arborescence de répertoires en cumulant les `../..`

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> on dit
parfois "lever une exception" / "raise an exception"
