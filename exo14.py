# Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher si ce nombre est carré parfait ou non
from math import *
n = int(input("Entrer un Nombre "))
N = n**2
if isinstance(N, (float)):
    print("c'est pas un carre parfait")
else:
    print("c'est un carre parfait")