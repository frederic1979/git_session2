periode = "a definir"
heure = 45

if heure < 10 :
    periode = "matinée"

elif heure < 15 :
    periode = "après midi"

elif heure < 0 :
    print("erreur de saisie")

elif heure > 24 :
    print("erreur de saisie")

print(f'bonne {periode}')
