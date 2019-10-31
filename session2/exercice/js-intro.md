# Exercices JavaScript

## Prise en main du langage

Pour vous familiarisez avec JavaScript, créez une page HTML basique avec un titre et un appel à un fichier JavaScript.

### Etape 1 : La base

Réalisez les fonctions suivantes en JavaScript :

* La fonction de base HelloWorld qui affiche une boite de dialogue avec "Hello World" en utilisant la fonction `alert()`
* Une fonction d'addition de 2 nombres en utilisant `prompt()`, la fonction devra afficher le résultat dans la page web
* Une fonction qui demande à l'utilisateur de saisir 5 nombres avec la fonction `prompt()` qui stocke les nombres dans un tableau, qui trie ce tableau et qui l'affiche dans la page HTML une fois trié

## Le DOM : Rendez votre IHM dynamique

### Etape 2 : Gestion des tickets dans votre documentation

Maintenant que vous savez tout ce qu'il est possible de faire avec JavaScript, vous allez devoir rendre votre documentation de mini projet dynamique.

Vous allez y ajouter un nouveau menu **Tickets** où vous allez ajouter un formulaire que l'utilisateur•ice pourra utiliser pour vous faire des retours (par exemple si je souhaite vous faire part d'un bug, d'une nouvelle feature, ...) et un tableau de tous les tickets postés. Il faudra que le formulaire de soumission de ticket soit composé :

* D'un champ **Prénom**
* D'un champ **Nom**
* D'un champ **Email**
* D'une liste déroulante définissant la **nature** du ticket (_bug_, _amélioration_, ...)
* D'une liste déroulante pour indiquer la **priorité** du ticket (_haute_, _normale_ ou _faible_)
* D'un champ texte pour la **description** du ticket

Lors de la soumission de ce formulaire, vous devrez récupérer le contenu du formulaire et ajouter une nouvelle entrée au tableau des tickets existants.

**Consignes :**

* Lorsqu'un utilisateur clic sur le bouton d'envoi du formulaire, annulez l'envoi grâce à `preventDefault`
* Utilisez un objet pour stocker le résultat de votre formulaire de saisie
* Ajoutez votre objet en tant que nouvelle ligne de votre table de données

### Etape 3 : Simulez une Single Page Application

Ajoutez différents liens dans votre application qui devraient normalement envoyer vers différentes pages HTML. Comme vous n'avez pas de serveur, vous allez devoir utiliser JavaScript pour recharger le contenu de votre page en fonctions des actions utilisateur.trice.
