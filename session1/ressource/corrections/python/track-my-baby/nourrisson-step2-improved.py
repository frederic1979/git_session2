# On importe les modules qui vont nous permettre de traiter les données
# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
# csv pour lire les fichiers de données
import csv

# Fonction de récupération du genre du nourrisson
def inputGender():
    while True:
        gender = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) : ")
        if gender.lower() == "g" or gender.lower() == "f":
            return gender
        else:
            continue

# Fonction de récupération des valeurs de référence
def get_standard_values(file_name):
    # On initialise des listes vides de valeurs de références
    age_values = []
    p5_values = []
    p25_values = []
    p50_values = []
    p75_values = []
    p95_values = []

    # On ouvre le fichier correspondant pour récupérer les valeurs
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            # On ignore la première ligne d'en-tête.
            if line_count == 0:
                line_count += 1
            else:
                age_values.append(float(row[0]))
                p5_values.append(float(row[1]))
                p25_values.append(float(row[2]))
                p50_values.append(float(row[3]))
                p75_values.append(float(row[4]))
                p95_values.append(float(row[5]))
                line_count += 1

        return { 'age': age_values, 'p5': p5_values, 'p25': p25_values, 'p50': p50_values, 'p75': p75_values, 'p95': p95_values }

def plot_values(standard_values, ages, measures, measure_name, measure_label, plot):
    plot.plot(standard_values['age'], standard_values['p5'], label=f'5% {measure_name}')
    plot.plot(standard_values['age'], standard_values['p25'], label=f'25% {measure_name}')
    plot.plot(standard_values['age'], standard_values['p50'], label=f'50% {measure_name}')
    plot.plot(standard_values['age'], standard_values['p75'], label=f'75% {measure_name}')
    plot.plot(standard_values['age'], standard_values['p95'], label=f'95% {measure_name}')
    
    plot.xlabel('Age en mois')
    plot.ylabel(measure_label)

    plot.scatter(ages, measures, c='black')

    plot.legend()
    plot.grid(True)


# On récupère le genre
gender = inputGender()

# On définit le nom des fichiers à ouvrir en fonction du genre
files = {
    'weight' : { 'g' : 'poids-age-garcon-0-60-light.csv', 'f': 'poids-age-fille-0-60-light.csv'},
    'height' : { 'g' : 'taille-age-garcon-0-60-light.csv', 'f' : 'taille-age-fille-0-60-light.csv'},
    'skull' : { 'g' : 'perim-cra-age-garcon-0-60-light.csv', 'f' : 'perim-cra-age-fille-0-60-light.csv'}
}

# On initilise des listes vides de mesures
values_ages = []
values_weight = []
values_height = []
values_skull = []

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

# On crée une figure sur laquelle on va afficher nos graphiques
plt.figure(figsize=(18, 8))

# On réalise le premier graphique avec le poids
plt.subplot(131)
standard_values_weight = get_standard_values(files['weight'][gender])
plot_values(standard_values_weight, values_ages, values_weight, 'poids', 'Poids en kg', plt)

plt.subplot(132)
standard_values_height = get_standard_values(files['height'][gender])
plot_values(standard_values_height, values_ages, values_height, 'taille', 'Taille en cm', plt)

plt.subplot(133)
standard_values_skull = get_standard_values(files['skull'][gender])
plot_values(standard_values_skull, values_ages, values_skull, 'périmètre cranien', 'Périmètre cranien en cm', plt)

# On affiche le graphique
plt.show()
