# On importe les modules qui vont nous permettre de traiter les données
# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv

# On demande le genre du nourrisson
def inputGender():
    while True:
        gender = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) : ")
        if gender.lower() == "g" or gender.lower() == "f":
            return gender
        else:
            continue

gender = inputGender()

# On initialise des listes vides de valeurs de références
p5_weights = []
p25_weights = []
p50_weights = []
p75_weights = []
p95_weights = []

p5_heights = []
p25_heights = []
p50_heights = []
p75_heights = []
p95_heights = []

p5_skulls = []
p25_skulls = []
p50_skulls = []
p75_skulls = []
p95_skulls = []

# On initilise des listes vides de mesures
values_ages = []
values_weight = []
values_height = []
values_skull = []

file_weight = ""
file_height = ""
file_skull = ""

# On définit le nom des fichiers à ouvrir en fonction du genre
if gender == "f":
    file_weight = "poids-age-fille-0-60-light.csv"
    file_height = "taille-age-fille-0-60-light.csv"
    file_skull = "perim-cra-age-fille-0-60-light.csv"

elif gender == "g":
    file_weight = "poids-age-garcon-0-60-light.csv"
    file_height = "taille-age-garcon-0-60-light.csv"
    file_skull = "perim-cra-age-garcon-0-60-light.csv"

# On récupère les valeurs de références provenant des fichiers
# Les poids
with open(file_weight) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count == 0:
            line_count += 1
        else:
            p5_weights.append(float(row[1]))
            p25_weights.append(float(row[2]))
            p50_weights.append(float(row[3]))
            p75_weights.append(float(row[4]))
            p95_weights.append(float(row[5]))
            line_count += 1

# Les tailles
with open(file_height) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count == 0:
            line_count += 1
        else:
            p5_heights.append(float(row[1]))
            p25_heights.append(float(row[2]))
            p50_heights.append(float(row[3]))
            p75_heights.append(float(row[4]))
            p95_heights.append(float(row[5]))
            line_count += 1

# Les périmètres craniens
with open(file_skull) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count == 0:
            line_count += 1
        else:
            p5_skulls.append(float(row[1]))
            p25_skulls.append(float(row[2]))
            p50_skulls.append(float(row[3]))
            p75_skulls.append(float(row[4]))
            p95_skulls.append(float(row[5]))
            line_count += 1

# on récupère les mesures
with open("mesures.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count == 0:
            line_count += 1
        else:
            values_ages.append(int(row[0]))
            values_weight.append(float(row[1]))
            values_height.append(float(row[2]))
            values_skull.append(float(row[3]))
            line_count += 1

# On crée un tableau de valeurs pour les ages (de 0 à 60 mois) => [0, 1, 2, ..., 58, 59, 60]
ages = range(61)

# On crée une figure sur laquelle on va afficher nos graphiques
plt.figure(figsize=(18, 8))

# On réalise le premier graphique avec le poids
plt.subplot(131)

plt.plot(ages, p5_weights, label='5% poids')
plt.plot(ages, p25_weights, label='25% poids')
plt.plot(ages, p50_weights, label='50% poids')
plt.plot(ages, p75_weights, label='75% poids')
plt.plot(ages, p95_weights, label='95% poids')
plt.xlabel('Age en mois')
plt.ylabel('Poids en kg')

plt.scatter(values_ages, values_weight, c='black')

plt.legend()
plt.grid(True)

# On réalise le second graphique avec la taille
plt.subplot(132)

plt.plot(ages, p5_heights, label='5% taille')
plt.plot(ages, p25_heights, label='25% taille')
plt.plot(ages, p50_heights, label='50% taille')
plt.plot(ages, p75_heights, label='75% taille')
plt.plot(ages, p95_heights, label='95% taille')
plt.xlabel('Age en mois')
plt.ylabel('Taille en cm')

plt.scatter(values_ages, values_height, c='black')

plt.legend()
plt.grid(True)

# On réalise le dernier graphique avec le périmètre cranien
plt.subplot(133)

plt.plot(ages, p5_skulls, label='5% périmètre cranien')
plt.plot(ages, p25_skulls, label='25% périmètre cranien')
plt.plot(ages, p50_skulls, label='50% périmètre cranien')
plt.plot(ages, p75_skulls, label='75% périmètre cranien')
plt.plot(ages, p95_skulls, label='95% périmètre cranien')
plt.xlabel('Age en mois')
plt.ylabel('Périmètre cranien en cm')

plt.scatter(values_ages, values_skull, c='black')

plt.legend()
plt.grid(True)

# On affiche le graphique
plt.show()
