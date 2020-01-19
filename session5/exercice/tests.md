# Tests unitaires en TDD

Tous les exercices suivants sont à faire en mode TDD. On écrit un test avant même d'avoir une fonction qui est écrite.

## Etape 1

### Smileys

On reprend l'exemple de la fonction qui permet de compter le nombre de smileys souriant dans une liste de chaînes de caractères. Cette fois on implémente la fonction en utilisant le TDD.

Un smiley est constitué de :

- une paire d'yeux `;` ou `:`
- un nez `-` ou `~` (optionnel)
- une bouche `)` ou `D`

Squelette de la fonction :

```java
public static int countSmileys(List<String> arr) {
  return null;
}
```

### CamelCase

Développer une fonction qui permet de transformer n'importe quelle chaîne de caractères en une nouvelle chaîne de caractères respectant le **CamelCase**.

Squelette de la fonction :

```java
public static String camelCase(String str) {
  return null;
}
```

### FizzBuzz

Développer une fonction qui prend en paramètres 2 entiers. Cette fonction retournera sous forme de chaine de caracatères tous les nombres entre min et max. Les multiples de 3 seront remplacés par Fizz, les multiples de 5 par Buzz et les multiples de 15 par FizzBuzz.

Exemple : l'appel de `fizzBuzz(1, 20);` doit retourner `12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19Buzz`

```java
public String fizzBuzz(int min, int max) {
  return null;
}
```

## Etape 2

Faire un (ou plusieurs) kata(s) de [Code Wars](https://codewars.com) en mode TDD.
