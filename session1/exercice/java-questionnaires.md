- [Contexte](#org7b1ba16)
- [Modélisation](#org6956ff5)
- [Implémentation préliminaire](#orgfe20e5a)
  - [Questions/ réponses/ nombre d'essais "en dur" dans le code](#org7b31736)
  - [Questions/ réponses/ nombre de points lus dans un fichier](#org075ab9c)
- [Réflexion sur l'architecture du programme](#orgb20fd6c)
- [Évolution](#org803b000)



<a id="org7b1ba16"></a>

# Contexte

On veut réaliser un programme de questionnaires, qui permette de poser des questions à l'utilisateur, la bonne réponse donnant une certain nombre de points.

À la fin d'une session, éventuellement en donnant plusieurs essais, le programme indique le score final, somme de tous les points obtenus pour toutes les questions.


<a id="org6956ff5"></a>

# Modélisation

Identifier les données manipulées par le programme et proposer des types pour les représenter en Java.


<a id="orgfe20e5a"></a>

# Implémentation préliminaire


<a id="org7b31736"></a>

## Questions/ réponses/ nombre d'essais "en dur" dans le code

Écrire un programme Java qui pose les questions suivantes :

-   "Quel langage à typage statique avez-vous vu en formation ?"
-   "Quel IDE utilisez-vous ?"
-   "Quel langage à typage dynamique avez-vous vu en formation ?"

Les réponses attendues étant (respectivement) :

-   "Java"
-   "IntelliJ"
-   "Python"

Et le nombre de points étant (respectivement) :

-   3
-   1
-   2


<a id="org075ab9c"></a>

## Questions/ réponses/ nombre de points lus dans un fichier

Modifier le programme pour qu'il lise les données dans un fichier. Quel format de fichier proposez-vous ?


<a id="orgb20fd6c"></a>

# Réflexion sur l'architecture du programme

En quoi les types primitifs ne sont-ils pas très satisfaisant pour représenter nos données ?


<a id="org803b000"></a>

# Évolution

On voudra avoir des questionnaires plus complexes, avec des rubriques, voire des sous-rubriques. Un questionnaire pourra par exemple :

-   commencer par une simple question (e.g. "Quel IDE utilisez-vous ?", pour 1 point)
-   Poursuivre par une rubrique (e.g. "Langages de programmation") contenant plusieurs questions (e.g. 2 questions "Quel langage à typage statique avez-vous vu en formation ?" et "Quel langage à typage dynamique avez-vous vu en formation ?", pour 3 et 2 points et donc un total de 5 points)
-   Puis d'autres questions ou rubriques.

Une rubrique peut contenir des questions et/ou des rubriques (elles-mêmes composées de questions et/ou rubriques, etc.).

Quelle modélisation proposez-vous ?
