# Angular acte 1

## Components

### Templates

C'est le fichier HTML de mon composant.

#### Interpolation

Si dans mon composant TS j'ai un attribut `moustache = 'Belle moustache';`

Alors je peux utiliser l'interpolation pour afficher son contenu dans le HTML.

`<p>{{ moustache }}</p>`

J'ai le droit de faire **plus** que juste afficher le contenu d'une variable.

Si dans mon composant TS j'ai un attribut `ig = 50;`

Alors je peux utiliser l'interpolation et faire un calcul dans le HTML.

`<p>{{ ig / 2 * 10 }}</p>`

#### Property binding

Cela permet d'écrire du code à interpréter comme valeur d'un attribut d'une balise HTML.

`<a [title]="product.name + ' details'">`

Dans cet exemple, l'attribut `title` de la balise `<a>` prendra la valeur de `product.name` concaténée à `' details'`.

#### Event binding

Cela permet de réagir aux évenements arrivant sur la page HTML.

`<button (click)="handlePurchase()">Purchase</button>`

Pour que cet exemple fonctionne, il faut que la fonction `handlePurchase()` soit déclarée dans mon composant TS.

#### Input

Permet de passer des informations / données d'un composant parent vers un composant enfant.

Dans le TS **enfant** il faut : `@Input() moustache: string`.

Pour que dans le HTML **parent** je puisse écrire :

`<app-enfant [moustache]="Belle moustache"></app-enfant>`

#### Output

_Devoir du week-end !_

### Component (TS)

Dans le composant TS on peut gérer le cycle de vie avec les **lifecycle hooks** (`ngOnInit()`, `ngOnChanges()`, `ngOnDestroy()`, ...).

### Style

RAS c'est du CSS.

## Service

C'est souvent dans les services que l'on va gérer les données.

On peut les injecter facilement grâce à l'injection de dépendances d'Angular :

```typescript
export class MyClass {
    constructor(private dataService: DataService)
}
```

**N.B.** : C'est équivalent à ce bout de Java (par rapport à l'injection de dépendances):

```java
public class MyClass {
    private DataService dataService;

    public MyClass(DataService dataService) {
        this.dataService = dataService;
    }
}
```
