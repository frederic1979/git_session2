# Etre un•e dévelopeur•euse éthique

> Un grand pouvoir implique de grandes responsabilités.

En devenant développeur•euse•s vous avez maintenant un **grand pouvoir** ! Vous êtes maintenant en capacité de créer des sites, des applications pour répondre à un besoin. Ce grand pouvoir implique de **grandes responsabilités**. Tout d'abord celle de développer en ayant en tête les critères de **performance** et **d'éco-conception**. Ensuite en gardant toujours à l'esprit qu'il peut y avoir des personnes avec un ou plusieurs **handicaps** qui utiliseront votre site ou application. Enfin vous devrez vous rappeler que, dans la majorité des cas, **les données de utilisateur•ice•s ne vous appartiennent pas** et si vous les stockez, traitez, transférez, ... vous devez vous plier au [Réglement Général pour la Protection des Données](https://www.cnil.fr/fr/reglement-europeen-protection-donnees).

## Développer green / performant

D'après [l'étude sur l'empreinte environnementale du numérique mondial](https://www.greenit.fr/etude-empreinte-environnementale-du-numerique-mondial/) ([du collectif Green IT](https://www.greenit.fr)) on a aujourd'hui : 34 milliards d’équipements pour 4,1 milliards d’utilisateurs, soit 8 équipements par utilisateur•ice. Toujours d'après cette étude, en 2019, la **consommation électrique des terminaux** est la **deuxième** source d'impact du numérique derrière la **fabrication des terminaux utilisateur•ice•s**. Vient ensuite en **troisième** position la **consommation électrique du réseau** puis la **consommation électrique des centres informatiques** (ou datacenters).

Rendez-vous compte du **pouvoir** (et donc des **responsabilités**) que vous avez ! Imaginez que votre application ou votre site web soit utilisé sur autant de terminaux et par autant de personnes. Imaginez que vous ayez oublié de supprimer des images (non compressées qui plus est) dont vous n'avez plus besoin sur votre site mais qu'elles sont toujours toujours téléchargées à chaque chargement de votre site ! Imaginez que vous ayez développé des fonctionnalités qui ne sont jamais utilisées mais qui pèse dans votre application (par le nombre de ligne de code, par la puissance du serveur requise, ...). Pensez un moment à **la consommation d'énergie que cela peut représenter** !

Si l'on ne fait pas attention, on contribue à **diminuer** la durée de vie des terminaux en les faisant "ramer" et à **augmenter** la consommation de ressources (puissance serveur, bande passante, ...) parce que notre application est "grasse".

Pour limiter ces effets, on peut heureusement appliquer des bonnes pratiques :

- De conception fonctionnelle :
  - Eliminer les fonctionnalités non essentielles (frugalité)
  - Quantifier précisement le besoin (sobriété)
- D'ergonomie :
  - Préférer la saisie assisté à l'autocomplétion
  - Favoriser un design simple, épuré, adapté au Web
  - Créer un site responsive
  - Respecter le principe de navigation rapide dans l'historique
- De conception technique :
  - Limiter le nombre de requête HTTP
  - Stocker les données statiques localement
- De conception graphique :
  - Préférer le CSS aux images
  - Limiter le nombre de CSS
  - Favoriser les polices standard
  - Ecrire des sélecteurs efficaces
- De développement :
  - Valider les pages auprès du W3C
  - Valider le code JavaScript
- D'hébergement :
  - Minifier les fichiers CSS
  - Minifier les fichiers JavaScript

... Bref il y en a [115 (des bonnes pratiques)](https://collectif.greenit.fr/ecoconception-web/115-bonnes-pratiques-eco-conception_web.html) conseillée par [le collectif Green IT](https://www.greenit.fr)

## Développer accessible

### C'est quoi l'accessibilité

Il s'agit de la **mise à disposition** des sites ou applications que vous développez **pour tous**. Cette mise à disposition doit prendre en compte les personnes en situation de handicap et aussi les personnes qui utilisent un téléphone mobile ou une connexion internet limitée en débit.

### Pourquoi le faire

Il est nécessaire de le prendre en compte pour plusieurs raisons :

- Parce que c'est faire preuve **d'éthique** et **de morale**
- Parce que souvent, cela participe à **l'optimisation** de votre site ou application
- Parce que ça devient **obligatoire** [Décret du 25 Juillet 2019](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000038811937&categorieLien=id)

### Pour quels handicaps

Pour en apprendre un peu plus sur les différents handicaps, vous pouvez lire [le tutoriel de MDN sur l'accessibilité](https://developer.mozilla.org/fr/docs/Apprendre/a11y/What_is_accessibility).

### Quand le faire

Il faut s'occuper de l'accessibilité de votre site ou application **dès le début** de votre projet. Comme les tests, si l'accessibilité est prise en compte dès le début, cela ne représente pas une charge de travail énorme. Si par contre vous attendez la fin d'un projet, cela risque d'être chronophage et pénible.

### Comment le faire

En appliquand respectant [les critères fourni par le W3C](https://www.w3.org/WAI/standards-guidelines/wcag/glance/) et [ceux du gouvernement français](https://references.modernisation.gouv.fr/rgaa-accessibilite/criteres.html)

Les critères à retenir :

- Utiliser la sémantique des balises HTML pour donner du sens à son contenu
- Définir un texte alternatif pour les images en utilisant l'attribut `alt` de la balise `img`
- Mettre du sens dans les éléments. Eviter à tout prix le `<a href="http://mysite.com/download">Cliquez ici</a>` pour proposer un téléchargement. Proposer plutôt : `<a href="http://mysite.com/download">Télécharger la plaquette récapitulant mes prestations</a>`
- Proposer une confirmation pour les actions impactantes (supprimer son compte, ...)
- Vérifier que la navigation est possible au clavier
- Développer mobile first
- Choisir une mise en page aérée
- Ne pas se baser uniquement sur l'aspect visuel du site ou de l'application

Pour plus de détails :

- [Gérer les problème courant d'accessibilité (MDN)](https://developer.mozilla.org/fr/docs/Learn/Tools_and_testing/Cross_browser_testing/Accessibilité)
- [Accessibility posters](https://ukhomeoffice.github.io/accessibility-posters/posters/accessibility-posters.pdf)

### Comment tester son application

Afin de vérifier si l'on est "dans les clous" niveau accessibilité, on peut utiliser des outils d'audit comme [Wave](http://wave.webaim.org/) ou des plugins pour les outils de développement du navigateur comme [aXe](https://www.deque.com/axe/). Cela permet de valider la _longue_ liste des critères.

## Développer en conformité avec le RGPD

### Qu'est ce que le RGPD

Le [Réglement Général pour la Protection des Données](https://www.cnil.fr/fr/reglement-europeen-protection-donnees) vise à encadrer les **traitements des données personnelles** et à harmoniser les lois au niveau européen. Toutes les personnes et entreprises gérant des données personnelles doivent s'y conformer.

### Qu'est-ce qu'une donnée personnelle

> Une « donnée personnelle » est « toute information se rapportant à une personne physique identifiée ou identifiable ».

C'est une définition très large. Il faut bien comprendre que l'on peut identifier une personne **directement** (avec son nom et son prénom) ou **indirectement** (avec son numéro de téléphone, son numéro de sécurité sociale, son adresse IP, ...). Cette identification peut se faire avec une donnée ou plusieurs (_une donnée_ : numéro de sécurité sociale, _deux données_ : combinaison de l'adresse et de la date de naissance d'une personne par exemple).

Tout est très bien expliqué dans [les bases du RGPD par la CNIL](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on).

### Qu'est-ce qu'un traitement d'une donnée personnelle

C'est ici aussi un concept très large. Il peut simplement s'agir d'un **stockage** d'une donnée, de sa **consultation**, de sa **comparaison** avec d'autres, de sa **transmission** ...

De la même manière tout est très bien expliqué dans [les bases du RGPD par la CNIL](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on).

### Le rôle du•de la développeur•euse

En tant que développeur•euse vous allez très probablement être amenés à gerer des données personnelles de vos utilisateurs. Dans ce cas, il convient d'avoir les [les bons reflexes](https://www.cnil.fr/fr/protection-des-donnees-les-bons-reflexes) pour assurer leur protection.

La CNIL a fait un super boulot en proposant un [kit RGPD pour les développeur•euse•s](https://www.cnil.fr/fr/kit-developpeur). Ce kit détaille les actions à mettre en oeuvre pour s'assurer de la bonne protection des données.

Ce dont il faut s'assurer :

- Que les choix des **outils de travail** sont en **conformité** avec la protection des données de vos utilisateurs
- Que vous développez en utilisant les concepts de **security by design** et **privacy by design** (c'est à dire en gérant la sécurité et la protection des données dès le début de votre projet en le gérant dès la conception)
- Que vos dépots ont les bonnes permissions, que vous ne stockez **pas de secrets en ligne** (type mot de passe de base de données)
- Que les librairies et frameworks que vous utilisez sont **à jour** (notamment en terme de sécurité)
- Que votre code est **propre** et bien **documenté**
