import math

def aire_triangle(base, hauteur):
    return base * hauteur / 2

def volume_sphere(rayon):
    return 4/3 * math.pi * rayon ** 3

def imc(taille, poids):
    calcul = poids / (taille / 100) ** 2
    return calcul

print(f'aire du triangle base 2 x et hauteur 7 : {round(aire_triangle(2, 7), 1)}')
print()
print(f'volume de la sphere de rayon 12 : {round(volume_sphere(12), 2)}')
print()
print(f"imc de Jules : {round(imc(184.5, 73), 1)}")
