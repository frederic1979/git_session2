# Debugguer un code qui n'est pas le sien

## Etape 1 : Debugguez le mien d'abord

Tous les programmes ci-dessous peuvent s'exécuter de manière indépendante. Il vous suffit de les importer dans votre IDE.

Votre mission est de débugguer mon code et de me dire pourquoi il ne fonctionne pas.

Il vous est évidemment **chaudement recommandé** d'utiliser le `debugger` de votre IDE préféré.

### Echauffement

Exercice 1_1 :

```java
public class Exercice1_1 {
  /**
   * J'ai un problème à l'exécution de ce programme Java.
   */
  public static void main(String[] args) {
    int[] numbers = new int[4];
    for (int i = 1; i < 5; i++) {
      System.out.println("About to try to insert " + i + " into the array at position " + i);
      numbers[i] = i;
      System.out.println("Successful");
    }

    System.out.print("This is what is in the array: ");
    for (int i = 1; i < 5; i++) {
      int element = numbers[i];
      System.out.print(element + " ");
    }
    System.out.println();
  }
}
```

Exercice 1_2 :

```java
public class Exercice1_2 {
  /**
   * Ce programme doit me retourner le complément d'une chaîne d'ADN mais ça ne fonctionne pas.
   */
  public static void main(String[] args) {
    System.out.println(makeDNAComplement("AATGCCGGC"));
    System.out.println(makeDNAComplement("TTACGGCCG"));
    System.out.println(makeDNAComplement("AATTCCGTACGGA"));
  }

  /**
   * Function that returns a DNA string complement.
   * 
   * @param dna the DNA string to complement.
   * @return complemented DNA string. Example : input ("AATGCCGGC") => output ("TTACGGCCG").
   */
  public static String makeDNAComplement(String dna) {
    String result = "";
    if (dna != null && !dna.isEmpty()) {
      char[] dnaCharArray = dna.toCharArray();

      for (char dnaChar : dnaCharArray) {
        switch (dnaChar) {
        case 'A':
          result = result.concat("T");
        case 'T':
          result = result.concat("A");
        case 'C':
          result = result.concat("G");
        case 'G':
          result = result.concat("C");
        }
      }
    }
    return result;
  }
}
```

### Renforcement musculaire

Exercice2_1 :

```java
public class Exercice2_1 {
  /**
   * Ce programme ne calcule pas comme il faut la factorielle d'un nombre.
   */
  public static void main(String[] args) {
    System.out.println(factorielleIte(5));
  }

  /**
   * Math factorial iterative implementation.
   * 
   * @param n factorial number to process.
   * @return n!
   */
  public static int factorielleIte(int n) {
    int result = 1;
    int i = 1;

    while (i <= n) {
      result *= i;
    }

    return result;
  }
}
```

Exercice2_2 :

```java
public class Exercice2_2 {
  /**
   * Ce programme m'affiche une jolie erreur. Que ce passe t-il ?
   */
  public static void main(String[] args) {
    System.out.println(fibonacciRec(5));
  }

  /**
   * Math function to find the nth Fibonacci number (recursive).
   *
   * @param n nth Fibonacci index
   * @return the nth Fibonacci number
   */
  public static int fibonacciRec(int n) {
    int result = 0;

    result = fibonacciRec(n - 1) + fibonacciRec(n - 2);

    return result;
  }
}
```

Exercice2_3 :

```java
public class Exercice2_3 {
  /**
   * Je veux que ce programme affiche un sapin de 20 ligne de haut mais ça ne fonctionne pas.
   */
  public static void main(String[] args) {
    System.out.println(drawTree(20));
  }

  /**
   * Function that draws a tree with height treeHeight.
   *
   * @param treeHeight the height of the tree to draw.
   * @return a String array containing each stage of the tree.
   */
  public static String[] drawTree(int treeHeight) {
    String[] tree = new String[treeHeight + 1];
    if (treeHeight > 4 && treeHeight < 26) {
      for (int i = 0; i < treeHeight; i++) {
        tree[i] = drawTreeStage(i + 1, treeHeight);
      }
      tree[treeHeight] = drawTreeStage(2, treeHeight);
    }

    return tree;
  }

  /**
   * Function that draws a stage of the tree.
   * 
   * @param stage the stage number to draw
   * @param treeHeight the tree height
   * @return a String representing the nth stage of the tree.
   */
  private static String drawTreeStage(int stage, int treeHeight) {
    String treeStage = "";
    int spaceNumber = treeHeight - stage;
    int hashTagNumber = 1 + 2 * (treeHeight - 1);

    for (int i = 0; i < spaceNumber; i++) {
      treeStage = treeStage + " ";
    }

    for (int i = 0; i < hashTagNumber; i++) {
      treeStage = treeStage + "#";
    }

    return treeStage;
  }
}
```

### Test MAX

Exercice3_1 :

```java
import java.util.Arrays;

public class Exercice3_1 {
  public static void main(String[] args) {
    int[] a = {1, 2, 3, 4, 5};
    System.out.println(Arrays.toString(transformation(a)));
  }

  public static int[] transformation(int[] a) {
    int t = a.length;
    int[] b = new int[t];
    int c = -1;

    c++;
    do {
      b[c] = a[--t];
      c++;
    } while (c < t);

    return b;
  }
}
```

## Etape 2 : Créez un algorithme buggué

Créez un algorithme buggué et demandez à votre voisin de résoudre le problème.

## Etape 3 : Débugguez celui de votre voisin

L'arroseur arrosé :-).
