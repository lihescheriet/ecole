# Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher la valeur de la somme 1 + 2 + … + n =
nb = int(input("Entrer un nombre"))
number = 0
number_one = 1
while number < nb:
    number += number_one
    print(number)
