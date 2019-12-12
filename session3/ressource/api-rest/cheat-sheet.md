# Cheat Sheet Spring boot

## Packages

**Attention !** Il est important de placer ses packages (_controller_, _model_, ...) sous le package principal pour que la découverte des composants se fasse. Si on ne fait pas ça, l'injection de dépendance ne pourra pas se faire.

- co.simplon.api
  - co.simplon.api.controller
  - co.simplon.api.model

## Controller

### @RestController

Annotation qui permet de simplifier la création de services REST qui combine @Controller et @ResponseBody. Cette annotation permet à Spring de charger la classe comme un **Controller** et donc d'utiliser les méthodes de la classe comme réponse aux appels HTTP (méthodes à combiner avec les annotations `@RequestMapping` ou `@GetMappting`, `@PutMappting`, `@PostMappting`, ...).

### @RequestMapping

Annotation qui permet de determiner le chemin d'accès aux ressources (ex : `/api/persons`).

Cette annotation peut s'utiliser sur :

- une classe : dans ce cas toutes les méthodes de la classe seront liées à une l'URL définie dans l'annotation.
- une méthode : dans ce cas, la méthode sera liée à l'URL définie dans l'annotation

En pratique, sur les méthodes on utilisera des annotations spécifiques avec les méthodes HTTP (`@GetMapping`, ...).

### @GetMapping

Annotation qui permet de définir qu'une méthode doit répondre à une requête GET.

### @PostMapping

Annotation qui permet de définir qu'une méthode doit répondre à une requête POST.

### @PutMapping

Annotation qui permet de définir qu'une méthode doit répondre à une requête PUT.

### @DeleteMapping

Annotation qui permet de définir qu'une méthode doit répondre à une requête DELETE.

### @RequestBody

Annotation permettant de spécifier qu'un argument d'une méthode doit être chargé avec le corps de la requête HTTP.

### @PathVariable

Annotation qui indique qu'un paramètre d'une URL doit être lié à un argument de méthode.

Exemple :

```java
@GetMapping("/{personId}")
public ResponseEntity<Person> getOne(@PathVariable Long personId){ ... }
```
