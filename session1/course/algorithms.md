# Les algorithmes "purs et durs"

## Définition d'un problème
### Qu’est ce qu’un problème ?
C'est une question à résoudre par des méthodes rationnelles ou scientifiques.

### Exemple 1 : Le problème du fermier sur la berge

Un fermier possède un renard, un canard et un sac de maïs. Il doit traverser une rivière avec un petit bateau disponible sur la berge. Le fermier a les contraintes suivantes :
  * le bateau ne permet d'emmener qu’un passager / objet à la fois.
  * le canard ne doit pas être laissé seul avec le maïs sinon il va manger le maïs
  * le renard ne doit pas être laissé seul avec le canard sinon le renard mangera le canard.

**Comment fait le fermier pour faire traverser tout le monde sans encombre ?**

_Retour sur l'exercice_ : Ce problème montre l’importance des contraintes (si on les supprime le problème n’en est plus un) et l’importance de connaître toutes les actions possibles pour résoudre un problème (si je vous dit au départ que vous pouvez revenir en arrière avec le canard ou le renard, alors vous résolvez le problème plus facilement).

_Solution_ :
Reformuler le problème et le regarder sous tous les angles avant de chercher la solution

### Exemple 2 : Une recherche documentaire

Il y a quelques années, lorsque nous n'utilisions pas d'outils numériques et que nous avions besoin de nouvelles connaissances, nous allions bien souvent vers une bibliothèque ou une librairie.

Imaginez que vous êtes dans les années 1970 et que recherchiez à en apprendre plus sur la culture Bouddhiste. Vous vivez dans une grande ville et vous savez que la bibliothèque municipale est grande et bien fournie. Vous décidez de prendre votre moyen de locomotion favori et vous vous rendez à la bibliothèque municipale. Lorsque vous arrivez, vous ne savez pas forcément comment trouver votre bonheur. Vous demandez alors à la personne responsable de la bibliothèque si elle peut vous aider.

**Que va t-elle faire ?** Elle va rechercher sur le plan de la bibliothèque où se trouve le rayon _religion et spiritualité_ et vous indiquera comment vous y rendre. Ensuite ce sera à vous de regarder dans le rayon de la bibliothèque. Vous regardez donc les étagères et constatez que des lettres y sont accrochées pour indiquer l'ordre alphabétique de rangement des livres. Vous vous arrêtez sur la lettre **B** et cherchez les livres traitant du Bouddhisme. Ensuite vous lisez les différents livres traitant du sujet.

Si l'on récapitule, pour chercher l'information, vous avez effectué plusieurs actions vous permettant de vous rapprocher petit à petit de l'information qui vous intéressait. On pourrait écrire lister nos actions de recherche de cette façon :

```
recherche d'information
  aller à la bibliothèque
  demander l'emplacement du rayon religion et spiritualité
  se déplacer dans le rayon
  rechercher par ordre alphabétique dans les étagères
  lire les livres traitant du sujet
```

_Retour sur l'exercice_ : Ce problème montre que l'on peut découper un problème en plusieurs sous-problèmes. C'est exactement ce qu'il se passe lorsque vous faites aujourd'hui une recherche sur un moteur de recherche. Les développeurs des moteurs de recherche découpent le problème de la recherche en petits problèmes qu'ils résolvent séparément (récupération de votre recherche, recherche dans leurs bases de données, présentation des résultats, ...).

### Exemple 3 : Itinéraire

Imaginez à nouveau que nous soyons dans les années 1970 et que nous cherchions à nous rendre chez notre meilleur ami qui vient de déménager à 500 kilomètres de chez nous. Nous possédons une voiture pour nous y rendre mais nous n'y sommes jamais allé. Comment être sur de prendre les bonnes routes pour s'y rendre en parcourant le moins de kilomètres possible ?

Afin de résoudre ce problème, nous allons consulter une carte ! Une fois la carte en main, nous allons rechercher à combiner les portions de route pour nous rendre chez notre ami tout en parcourant le moins de kilomètres possible.

En consultant la carte, nous allons identifier notre point de départ et notre point d'arrivée. Ensuite, nous allons rechercher à rejoindre ces deux _noeuds_ (les points de départ et d'arrivée) par des _liens_ (les portions de routes). Sur notre route nous allons rencontrer d'autres noeuds (qui seront des intersections entre les différentes routes) et à chaque intersection, nous allons devoir décider quel nouvelle portion de route suivre. Ce qui nous permettra de décider quelle portion de route suivre sera à quelle point elle nous rapproche de notre point d'arrivée. Nous le faisons bien souvent de manière assez intuitive et nous n'analysons pas tous les chemins possible, ce qui fait que nous n'avons pas forcément le chemin le plus cours.

Aujourd'hui, lorsque nous utilisons un GPS, c'est notre téléphone ou notre ordinateur qui fait ces calculs pour nous. Il va passer en revue tous les liens qui permettent de se rapprocher de notre destination. Il gardera au final l'enchaînement de liens qui fera le trajet le plus court.

**Plus d'infos** : [L'algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)

### Les clés pour solutionner un problème :
* **Toujours avoir un plan** (même si le plan risque d’être modifié, cela permet de définir des étapes intermédiaires et de suivre l’avancement de la résolution)
* **Reformuler le problème** (toujours la première étape du plan !). Cela permet à minima de s’assurer qu’on a compris le problème et parfois de voir le problème sous un autre angle et de trouver plus facilement une solution
* **Diviser le problème** (cela permet souvent de le simplifier). Exemple avec le tri de livres par hauteur, il vaut mieux trier 100 livres en découpant 25 par 25 puis rassembler les 4 x 25 triés que de trier les 100 d’un coup.
* **Commencer par ce que l’on sait faire**
* **Simplifier le problème** (parfois il est préférable de supprimer des contraintes pour avoir une solution intermédiaire plus simple, même si elle ne couvre pas tout le problème).
* **Chercher les analogies** (ne veut pas dire copier/coller).
* **Expérimenter** (ne veut pas dire deviner ou faire “au pif”).
* **Garder la motivation** (éviter de laisser la frustration vous atteindre). Soyez indulgent avec vous même !

**Littérature** : [Think Like A Programmer An Introduction To Creative Problem Solving (V. Anton Spraul)](https://www.nostarch.com/thinklikeaprogrammer)

## Qu’est ce qu’un algorithme ?
Il s’agit d’une suite (finie) d’opérations élémentaires qui permettent de résoudre un problème. C’est une procédure de calcul qui prend en entrée un ensemble E de valeurs et qui retourne en sortie en ensemble E’ de valeurs.

Un algorithme doit toujours se terminer et fournir un résultat. Un algorithme est dit **correct** si pour chaque ensemble de valeurs **E** en entrée il fournit le même ensemble de résultat **E'** en sortie. Afin de s'assurer qu'un algorithme est correct, on peut le prouver de manière formelle. On utilise parfois certains algorithmes non corrects si l'on sait gérer le taux d'erreur de l'algorithme.

_Attention_ : certains problèmes ne sont **pas calculables**, il n'existe pas d'algorithme qui permette leur résolution.

### Exemples de problèmes calculables

**_Exemple 1 : La recette de cuisine_**

_Problème_ : mes enfants ont faim et veulent manger vite. J'ai seulement des pâtes crues dans mon placard. Que faire ?

_Solution_ : Préparer les pâtes

```
début
  remplir_casserole(eau)
  tant_que (eau_non_bouillante)
    chauffer_casserole(feu_max)
  fin_tant_que

  remplir_casserole(pâtes)
  tant_que (pâtes_non_cuites)
    chauffer_casserole(feu_fort)
  fin_tant_que

  égouter_pâtes
  servir_pâtes
fin
```

**_Exemple 2 : Le calcul du PGCD_**

_Problème_ : Comment calculer le plus grand commun diviseur de 2 nombres ?

_Solution_ : Utiliser la méthode Euclidienne !

```
début
  nb_1, nb_2
  max = max(nb_1, nb_2)
  min = min(nb_1, nb_2)
  reste = max modulo min
  tant_que (reste différent de zéro)
    max = min
    min = reste
    reste = max modulo min
  fin_tant_que

  pgcd = min
fin
```

### Les structures algorithmiques
Dans les 2 exemples utilisés pour illustrer un algorithme on remarque que :
* certaines opérations élémentaires sont répétées tant qu'une condition est vrai. On utilise ici le concept de structure de contrôle.
* on "stocke" certaines informations qu'on utilise à nouveau par la suite. On utilise ici le concept de structure de données.

#### Les structures de contrôle
Les structures de contrôle permettent en fait à l'algorithme de prendre un décision (grâce aux conditions) et/ou de répéter certaines opérations (grâce aux boucles).

#### Les structures de données
Les structures de données permettent le stockage de l'information. Elles sont utilisées pour organiser les données afin de pouvoir les traiter le plus facilement possible. On utilisera très souvent les constantes, les variables, les tableaux, les listes. On utilisera parfois les arbres, les graphes, ...

Pour plus de détails :
* [Les structures de contrôle sur Wikipedia](https://fr.wikipedia.org/wiki/Structure_de_contr%C3%B4le)
* [Les structures de données sur Wikipedia](https://fr.wikipedia.org/wiki/Structure_de_donn%C3%A9es)

#### Traiter un ensemble de données : décomposition

Généralement, s'il n'y a qu'une seule valeur traiter, il est possible de le faire directement. Pour traiter des ensembles de valeurs, il y a principalement deux façon de décomposer :

##### Itérations
On traite les valeurs les unes après les autres. On initialise le résultat avec la valeur correspondant à un ensemble vide, puis, pour chacune des valeurs à traiter, on met à jour ce résultat.

Par exemple, pour calculer la somme des valeurs, on initialise le résultat à 0 et l'on additionne successivement chacune des valeurs au résultat partiel :

```
début
  xs
  somme = 0
  pour_chaque x de xs :
    somme = somme + x
  fin_pour_chaque
fin
```

##### Récursion

On traite les valeurs par sous-ensemble (par exemple par moitiés), sauf si l'ensemble à traiter est trivial (un seul élément) et l'on combine les résultats sur les sous-ensembles.

Par exemple, pour calculer la somme des valeurs, si l'ensemble est vide la somme est 0, s'il contient une valeur c'est celle-ci, sinon c'est la somme des sommes des deux moitiés :

```
début
  xs
  si xs est vide :
    somme = 0
  sinon
    si xs contient un seul élément x :
      somme = x
    sinon
      somme1 = somme de la première motié
      somme2 = somme de la deuxième moitié
      somme = somme1 + somme2
    fin_si
  fin_si
fin
```

### Nos amies les machines
Grâce à nos machines (ordinateurs, calculateurs, microprocesseurs, ...), nous pouvons aujourd'hui (et depuis quelques décennies) leur demander de résoudre les algorithmes à notre place. Ceci grâce aux langages de programmation qui nous permettent de traduire nos algorithmes de calcul en langage compréhensible par la machine.

Dans la pratique lorsque nous faisons du developpement Web, on prouve rarement un algorithme. En effet, il s'agit peu souvent d'applications critiques et nous "faisons confiance" à notre code.

Le développement Web n'est peut-être pas le plus exigeant en ce qui concerne les preuves algorithmiques mais nous devons bien avoir conscience de la notion de complexité algorithmique. En effet ne pouvons pas demander tout et n'importe quoi à notre machine car, comme nous, elle a des limites en temps d'exécution et en mémoire.

**La notion de complexité** : Il s'agit en fait de l'efficacité de l'algorithme qu'on va développer. On cherche à prévoir le nombre d'opérations que va effectuer notre algorithme en fonction du volume de données qu'on lui fournit en entrée, et la place mémoire dont il va avoir besoin.

C'est important aussi en développement Web car les calculs se font majoritairement sur votre serveur, donc plus vos algorithmes seront rapides et plus votre serveur le sera.

Pour plus de détails :

* [La complexité algorithmique avec exemple sur OpenClassrooms](https://openclassrooms.com/courses/decouvrez-le-fonctionnement-des-algorithmes/comprenez-la-complexite-algorithmique)
* [La complexité algorithmique sur Wikipedia](https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes)

**_Les applications d'algo_**

* GPS
* Routage internet
* Cryptographie (banque, ...)
* Recherche dans un moteur de recherche

**_Attention_** : lorsque vous allez programmer, vous aurez peut-être tendance à oublier la notion d'algorithme et à écrire du code avant même de réfléchir au problème à résoudre.
