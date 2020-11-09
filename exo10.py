# Ecrire un programme en Python qui demande à l’utilisateur de saisir le rayon d’un cercle et de lui renvoyer la surface et le périmètre.
from math import *
R = int(input("Entrer le Rayon du Cercle !"))
print("Le Périmetre du Cercle est ", 2*pi*R)
R = R**2
A = R * pi
print("La Surface est de ", A)
