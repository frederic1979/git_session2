# Créer un programme qui demande à l'utilisateur de se présenter : prénom, nom et age.
# Utilisez la console pour afficher un message d'accueil personnalisé du type
# "Bonjour Jules Grand tu as 30 ans c'est bien ça ?"
def dire_bonjour(nom, prenom, age):
    return f"Bonjour {prenom} {nom} tu as {age} ans, c'est bien ça ?"

print("---------- Mode console ----------")
prenom = input("Bonjour, quel est ton prénom ? ")
nom = input("Bonjour, quel est ton nom ? ")
age_utilisateur = 2019 - int(input("En quelle année es-tu né•e ? "))

print(dire_bonjour(nom, prenom, age_utilisateur))

# Créer un programme qui fera la même chose tout en écrivant les informations reçues
# dans un fichier texte. Le fichier devra être nommé prenom-nom.txt
print("\n---------- Mode fichier ----------")
nom_complet = input("Bonjour, comment t'appelles-tu ? ")
age_utilisateur = int(input("Quel age as-tu ? "))

with open(f'{nom_complet}.txt', 'w') as f:
    f.write(f"{nom_complet} a {age_utilisateur} ans !")

# Créer un programme qui va lire le fichier ../../../films-2018.txt
# et indiquer combien il y a de films sortis en 2018.
print("\n---------- Lecture films ----------")
nb_films = 0
films = []

with open('../../../films-2018.txt', 'r') as f:
    films = f.readlines()

with open('../../../films-2018.txt', 'r') as f:
    for line in f:
        nb_films = nb_films + 1

print(f'Nombre de films (avec la longueur de la liste) : {len(films)}')
print(f'Nombre de films (avec la boucle) : {nb_films}')

# Créer un programme qui va lire le fichier ../../../villes-france.txt
# et indiquer combien de fois apparaît TOULOUSE dans le fichier.
oh_toulouse = 0

with open('../../../villes-france.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.rstrip()
        if ligne == 'TOULOUSE' :
            oh_toulouse = oh_toulouse + 1

print("\n---------- Comptage TOULOUSE ----------")
print(f"TOULOUSE apparaît {oh_toulouse} fois dans le fichier.")

# Créer un programme qui va lire le fichier ../../../villes-france.txt
# et créer un nouveau fichier sans doublons
# (après modification, le nouveau fichier ne doit contenir
# qu'une seule fois le même nom de ville).
villes = []

fichier_propre = open('villes-france-clear.txt', 'w')

with open('../../../villes-france.txt', 'r') as f:
    for ligne in f:
        if ligne not in villes:
            fichier_propre.write(ligne)
            villes.append(ligne)

fichier_propre.close()

# Créer un programme qui va lire le fichier ../../../villes-france.txt
# et créer un nouveau fichier dans lequel chaque ligne donnera
# le nom d'une ville en affichant le nombre d’occurrence dans
# le fichier de départ. Ce fichier devra être trié par ordre
# alphabétique.

villes = {}

fichier_propre = open('villes-france-comptees.txt', 'w')

with open('../../../villes-france.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.rstrip()
        if ligne not in villes:
            villes[ligne] = 1
        else :
            villes[ligne] = villes[ligne] + 1

for nom_ville in villes.keys() :
    fichier_propre.write(f'{nom_ville} : {villes[nom_ville]} occurences.\n')

fichier_propre.close()
