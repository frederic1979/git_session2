# Créer une liste qui contient tous les prénoms du groupe.

prenoms_promo = ["Andrea", "Carole", "Nicolas", "Franck L", "Franck T", "Vincent", "Jean-Marc", "Nicolas", "Guillaume",
"Philippe", "Yves", "Benoît", "Pierre", "Sylvain", "Frédéric"]

print(prenoms_promo)
print()

# Trier cette liste.
prenoms_promo.sort()
print(prenoms_promo)
print()

# Afficher tous les prénoms qui ont un indice impair.
print(prenoms_promo[1 : : 2])
print()

# Créer deux sous-listes groupe_1 et groupe_2 contenant chacun la moitié du groupe.
taille_groupe = len(prenoms_promo)
groupe_1 = prenoms_promo[0 : taille_groupe // 2]
groupe_2 = prenoms_promo[taille_groupe // 2 : taille_groupe]

print(groupe_1)
print(groupe_2)

# Correction de l'exercice maudit
def affiche_numero_couleur(carte_nb) :
    couleur = ["pique", "coeur", "carreau", "trefle"]
    valeur = ["7", "8", "9", "10", "valet", "dame", "roi", "as"]

    couleur_nb = carte_nb // 8
    valeur_nb = carte_nb % 8

    print("la carte est : "+valeur[valeur_nb] + " de " + couleur[couleur_nb])

print()
affiche_numero_couleur(28)