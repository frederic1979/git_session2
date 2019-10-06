- [Pourquoi tester ?](#org71f2a59)
- [Que tester ?](#org19d80e7)
- [Comment tester ?](#orge981149)
- [Outils pour tester](#orgd786f88)
  - [Automatisation](#org250ef3e)
  - [Frameworks de test](#org35b8c50)



<a id="org71f2a59"></a>

# Pourquoi tester ?

Quand on écit un programme, on voudrait avoir des raisons de croire qu'il est correct ! Malheureusement, la plupart des langages de programmation ne peuvent même pas garantir que (x + 1) > x, à cause des [dépassements de capacité](https://fr.wikipedia.org/wiki/D%C3%A9passement_d%27entier), ou que 3\*(1/10) = 3/10, à cause des [erreurs de représentation](https://fr.wikipedia.org/wiki/IEEE_754) :

```java
public class BadMathDemo {
    public static void main(String[] args){
	int i = Integer.MAX_VALUE;
	System.out.println("i+1 > i ? " + ((i+1) > i));
	System.out.println("3*(1./10) == 3./10 ? " + ((3*(1./10)) == (3./10)));
    }
}
```

i+1 > i ? false 3\*(1./10) == 3./10 ? false

Donc évidemment, on ne peut pas prouver grand chose quand à l'exactitude d'un programme écrit dans un tel langage <sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>. Faute de preuves, on cherche à se donner des raisons de croire qu'un programme fonctionne correctement en le testant. Mais si des tests peuvent prouver la présence de bugs, ils ne peuvent pas prouver leur absence. En pratique, on considère qu'un programme est suffisamment peu buggé lorsque la vitesse de découverte de bugs et leur gravité sont suffisamment faibles.


<a id="org19d80e7"></a>

# Que tester ?

Si à terme il faudra bien tester le programme, voire le système auquel s'intègre le programme, on commence par tester les unités fonctionnelles les plus petites. On s'intéressera dans un premier temps aux [tests unitaires](https://fr.wikipedia.org/wiki/Test_unitaire). On va tester les fonctions/méthodes et les classes.

Pour qu'une fonction soit plus facilement testable, on voudra qu'elle soit [pure](https://fr.wikipedia.org/wiki/Fonction_pure) autant que possible :

-   il est plus facile de passer des arguments que de construire un état du système
-   il est plus facile de valider un résultat calculé que de constater un effet produit

On voudra tester toutes les lignes du code à tester, ce qui n'est pas évident à cause des structures de contrôle, d'où la notion de [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code) qui caractérise le pourcentage de code qui est effectivement exécuté par les tests.


<a id="orge981149"></a>

# Comment tester ?

Pour essayer de s'assurer qu'on [introduit pas de bugs](https://fr.wikipedia.org/wiki/Test_de_r%C3%A9gression), on a besoin de répéter les tests à chaque modification. Par ailleurs, on veut pouvoir tester différentes configurations (de systèmes d'exploitations, de versions de logiciels,…). Il est donc essentiel de pouvoir **automatiser** les tests. Les tests doivent donc être des programmes qui peuvent être lancés automatiquement, par exemple à chaque commit, voire compilation.

Pour chaque fonction à tester, on va déterminer un ensemble de valeurs d'arguments pour lesquels on va s'assurer que la fonction retourne bien le résultat attendu. On choisit ces arguments de façon à essayer de tester les cas particuliers et maximiser la couverture de code.

-   **Exercice:** Écrire un ou des programmes de tests qui teste[nt] chacune des fonctions implémentées.


<a id="orgd786f88"></a>

# TODO Outils pour tester


<a id="org250ef3e"></a>

## Automatisation

À terme, on pourra utilisera des outils d'[Intégration Continue](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue), par exemple [Github Actions](https://github.com/bhugueney/testing-actions-for-java-tests/commit/0660a23706633c491830459b48a1f11a5d77f3cd/checks?check_suite_id=221096623) pour automatiser l'exécution des tests.


<a id="org35b8c50"></a>

## Frameworks de test

On utilisera des frameworks de tests, par exemple [JUnit 5](http://www.jmdoudoux.fr/java/dej/chap-junit5.htm), pour automatiser l'écriture des tests.

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> d'autres
langages (par exemple [Coq](https://fr.wikipedia.org/wiki/Coq_(logiciel))) sont prévus pour ça
