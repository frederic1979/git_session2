# Exercices base de données relationnelle

## Etape 1 : Setup de la base

### Installation d'une base postgresql

- Pour installer postgresql sur un poste Ubuntu : `sudo apt install postgresql`.
- Pour installer postgresql sur un poste Windows :
  - [Téléchargement de la base](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
  - [Procédure d'installation](https://www.enterprisedb.com/edb-docs/d/postgresql/installation-getting-started/installation-guide-installers/12/PostgreSQL_Installation_Guide.1.07.html)

### Récupération de l'environnement de dev

[DataGrip](https://www.jetbrains.com/datagrip/)

### Création d'un rôle

On va créer un rôle pour utiliser avec la base de données avec DataGrip.

`sudo -u postgres createuser --interactive -P`

- `name of role` => db-user
- `password` => _up to you_
- `superuser` => no
- `create database` => yes
- `create new roles` => no

Une fois ceci fait, on peut utiliser DataGrip pour manipuler nos bases, créer des tables, ...

### Création d'une base

![Add database DataGrip](../ressource/add-pg-datagrip.png)

![Configure database DataGrip](../ressource/config-pg-datagrip.png)

## Etape 2 : Création d'une base à partir d'un modèle de données

Votre mission si vous l'acceptez : recréer la base de données d'Instagram !

On appellera cette base : `instagram`.

#nofilter

### Création de la base

A partir du diagramme de classe ci-dessous : créer le script SQL qui permettra de créer la structure de la base de données.

![Diagramme de classe UML Instagram](../ressource/insta-class-diagram.png)

### Validation de la base

Essayez :

- d'insérer des données dans la table `photos` avant la table `users` (assurez vous que ça ne passe pas)
- d'insérer des `users` puis des `photos`
- d'insérer des `hashtags`
- de faire des liens entre des `photos` et de `hashtags`
- d'insérer des `comments` liés à des `photos`
- d'insérer des `likes` liés à des `photos` et des `users`
- de supprimer un `user` qui possède plusieurs `photos` et assurez vous que :
  - les `photos` associées au `user` sont supprimées
  - les `comments` associés aux `users` sont supprimées
  - les `likes` associés aux `users` sont supprimées
  - les `comments` associés aux `photos` associées aux `users` sont supprimées
  - les `likes` associés aux `photos` associées aux `users` sont supprimées

## Etape 3 : Requêtage d'une base

Vous allez devoir créer et remplir une nouvelle base de données : `simplon_airlines` grâce à ce script : [DDL Simplon Airlines](../ressource/bdd/simplon_airline.sql).

Ensuite vous aurez pour mission de réaliser les requêtes suivantes :

### 1. Affichage des marques des avions

Résultat attendu _(2 lignes)_ :

| name |
| :--- |
| Airbus |
| Boeing |

### 2. Affichage des modèles d'avion Boeing

Résultat attendu _(14 lignes)_ :

| name |
| :--- |
| 247 |
| 307 |
| 314 |
| 377 |
| 707 |
| 717 |
| 720 |
| 727 |
| 737 |
| 747 |
| 757 |
| 767 |
| 777 |
| 787 |

### 3. Affichage des villes couvertes et leurs pays

Résultat attendu _(400 lignes)_ :

| pays | ville |
| :--- | :--- |
| Albania | Bërxull |
| Albania | Libofshë |
| Albania | Poroçan |
| Angola | Lucapa |
| China | Anjia |
| ... | ... |
| Vietnam | Tân Hiệp |
| Vietnam | Thị Trấn Na Hang |
| Vietnam | Thị Trấn Thọ Xuân |
| Vietnam | Tiền Hải |

### 4. Affichage des avions AIRBUS ayant plus de 300 places triés par nb de places décroissant

Résultat attendu _(63 lignes)_ :

| registration | seats_nb | name | name |
| :--- | :--- | :--- | :--- |
| FHN | 594 | Airbus | A340 |
| GBG | 593 | Airbus | A340 |
| YFX | 592 | Airbus | A318 |
| ... | ... | ... | ... |
| IXP | 315 | Airbus | Beluga |
| RZD | 312 | Airbus | A319 |
| QHI | 304 | Airbus | A321 |
| GXE | 302 | Airbus | A380 |

### 5. Affichage des vols intérieurs (même pays)

Résultat attendu _(41 lignes)_ :

| name | name | name |
| :--- | :--- | :--- |
| China | Dongfanghong | Dingbao |
| China | Shuigou | Hongqiao |
| China | Luntai | Xiangshui |
| ... | ... | ... | ... |
| Sweden | Solna | Tyresö |
| China | Xiongchi | Chengjiao |
| China | Liulin | Jingzhou |
| China | Haikoudajie | Longxing |
| Philippines | Himaya | Villa Aglipay |

### Affichage des vols intérieurs plus longs que 5h triés par durée décroissante

Résultat attendu _(17 lignes)_ :

| name | name | name | hour_duration |
| :--- | :--- | :--- | :--- |
| China | Oroin Xibe | Daxi | 9 |
| Philippines | Himaya | Villa Aglipay | 9 |
| China | Dongfanghong | Chengbei | 9 |
| China | Daijiaba | Dabachang | 9 |
| China | Shuigou | Hongqiao | 8 |
| China | Liulin | Yashao | 8 |
| China | Changliang | Lubao | 8 |
| China | Tuanchengshan | Ha’erlong | 7 |
| China | Yushan | Shuigou | 6 |
| China | Tianyu | Zhujiachang | 6 |
| China | Haikoudajie | Longxing | 6 |
| Poland | Witkowo | Leśnica | 6 |
| Japan | Kashima-shi | Menuma | 6 |
| China | Xiaohebian | Qiaotou | 6 |
| China | Lubao | Dabachang | 5 |
| Sweden | Solna | Tyresö | 5 |
| China | Rangxi | Chuoyuan | 5 |

### Afficher les 5 vols ayant le plus de personnel navigant

Résultat attendu _(5 lignes)_ :

| from_city | to_city | employee_count |
| :--- | :--- | :--- |
| Colorado Springs | Kingersheim | 7 |
| Yūki | Yushan | 6 |
| Fontenay-sous-Bois | Rochester | 6 |
| Bjuv | Edosaki | 5 |
| Yujiawu | Nîmes | 5 |
