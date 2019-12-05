- [Maven pour la gestion de dépendances](#org88b7739)
- [En pratique](#org1a2a876)
  - [Création du projet Maven](#orga3aa49f)
  - [Ajout d'une dépendance](#orgc3f068b)



<a id="org88b7739"></a>

# Maven pour la gestion de dépendances

[Maven](https://fr.wikipedia.org/wiki/Apache_Maven) est un outils de construction (*build*) de projets java. Il permet de gérer notamment, mais pas seulement, les dépendances (i.e. bibliothèques) en téléchargeant automatiquement celles-ci et en gérant le `CLASSPATH` pour que celles-ci soient directement utilisables.

La configuration de Maven est gérée par un fichier au format XML : `pom.xml`.

Les dépendances sont indiquées dans un bloc `dependencies` :

```nxml
<dependencies>

    <!-- les dépendances sont indiquées ici -->

</dependencies>

```

Chaque dépendance est indiquée dans un bloc `dependency` :

```nxml
    <dependency>

    <!-- la dépendance est indiquée ici -->

    </dependency>
```

Les informations caractérisant la dépendance sont :

-   **groupId:** identifie l'organisme qui publie la bibliothèque.
-   **artifactId:** identifie la bibliothèque parmi celle publiées par l'organisme.
-   **version:** indique la version de la bibliothèque à utiliser.


<a id="org1a2a876"></a>

# En pratique


<a id="orga3aa49f"></a>

## Création du projet Maven

Sous l'environnement de développement (e.g. Eclipse ou IntelliJ), lors de la création du projet, choisir un projet Maven. Par exemple sous IntelliJ `File` &rarr; `New` &rarr; `Project…`, choisir `Maven` dans la marge de gauche.

Dans un premier temps, on ne choisira pas d'archetype. Le projet maven a alors un `GroupId`, un `ArtifactId` et une version, comme les dépendances. Par défaut, l'`ArtifactId` est le nom du projet.

-   **Exercice:** Créer un projet maven appelé `TestMavenCsv` (Choisir `Enable Auto-Import` lorsque cela est proposé).


<a id="orgc3f068b"></a>

## Ajout d'une dépendance

Dans le fichier `pom.xml`, ajouter un bloc `<dependencies> </dependencies>`.

Ensuite, on va chercher les informations pour indiquer une dépendance envers une bibliothèque d'utilisation de fichiers au format csv, [Apache Common CSV](http://commons.apache.org/proper/commons-csv/). Il suffit de [chercher sur le site mvnrepository.com](https://mvnrepository.com/search?q=apache+common+csv) pour trouver [la page avec les informations nécessaires](https://mvnrepository.com/artifact/org.apache.commons/commons-csv) :

```nxml
<!-- https://mvnrepository.com/artifact/org.apache.commons/commons-csv -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-csv</artifactId>
    <version>1.7</version>
</dependency>
```

On peut ensuite écrire le code suivant :

```java
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;

import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static String[] HEADERS = {"nom_commune", "latitude", "longitude"};
    static Map<String, double[]> nameToCoords = new HashMap<String, double[]>();

    static {
        nameToCoords.put("Attignat", new double[]{46.283333, 5.166667});
        nameToCoords.put("Beaupont", new double[]{46.4, 5.266667});
        nameToCoords.put("Bény", new double[]{46.333333, 5.283333});
    }

    public static void main(String[] args) throws IOException {
        FileWriter out = new FileWriter("communes_new.csv");
        try (CSVPrinter printer = new CSVPrinter(out, CSVFormat.DEFAULT
                .withDelimiter(';').withHeader(HEADERS))) {
            for (Map.Entry<String, double[]> city : nameToCoords.entrySet()) {
                double[] coords = city.getValue();
                printer.printRecord(city.getKey(), coords[0], coords[1]);
            }
        }
    }
}

```

Attention ! :: IntelliJ [oblige à modifier la configuration pour que le programme puisse s'exécuter](https://youtrack.jetbrains.com/issue/IDEA-222668). (`File` &rarr; `Settings…` &rarr; `Build, Execution, Deployment` &rarr; `Compiler` &rarr; `Java Compiler` &rarr; `Per-module bytecode version` , mettre le `Target bytecode version` à 1.8 au moins).

Le programme peut être compilé et exécuté, Maven gérant automatiquement la dépendance à la bibliothèque `Apache Commons CSV`.

-   **Exercice:** Compiler et exécuter le code.
