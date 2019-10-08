maximum = 0
plus_long_prenom = ""

# Parcourir la liste précédente. Pour chaque prénom, afficher la longueur du prénom avec la fonction len.
prenoms_promo = ["Andrea", "Carole", "Nicolas", "Franck L", "Franck T", "Vincent", "Jean-Marc", "Nicolas", "Guillaume",
"Philippe", "Yves", "Benoît", "Pierre", "Sylvain", "Frédéric"]
prenoms_promo.sort()

for prenom in prenoms_promo :
    print(f'{prenom} fait {len(prenom)} caractères.')

# Pour chaque prénom, si la longueur du prénom est supérieur au maximum, remplacer maximum par cette valeur.
for prenom in prenoms_promo :
    if len(prenom) > maximum :
        maximum = len(prenom)
        plus_long_prenom = prenom

# Afficher le prénom le plus long à la fin avec un message : "le prénom le plus long est <prénom>, il possède lettres"

print(f'Le plus long prénom est : {plus_long_prenom}')

max = 0
maxprenom = []
for prenom in prenoms_promo: 
    ln_prenom= len(prenom)
    # print(prenom, " fait  " ,ln_prenom, " caractères" )
    if ln_prenom > max :
        max = ln_prenom
        maxprenom = []
        maxprenom.append(prenom)
    elif  ln_prenom == max :
        maxprenom.append(prenom)

if len(maxprenom)==1:
    print("le prénom le plus long est ", maxprenom , " , il possède " + str(max) + " lettres")
else:
    print("les prénoms les plus long sont : ")
    for prenom in maxprenom:
        print(prenom)
    print(" il possède " + str(max) + " lettres")