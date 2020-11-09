# Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher si ce nombre est premier ou non.
from math import *
n = int(input("Entrer un Nombre "))
# diviser par 1 et lui meme

print('Le programme est en train de vérifier si ce nombre est premier...')

i = 2

while i < n and n % i != 0 :

    i = i + 1

if i == n :

    print('Le nombre', n, 'est premier ! Fantastique !')

else :

    print('Ce n\'est pas un nombre premier.')