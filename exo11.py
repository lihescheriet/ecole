# Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher tous les diviseurs de ce nombre.

n = int(input("Entrer un Nombre !"))

diviseur=[]

for i in range(1, n + 1):
    if n % i == 0:
        diviseur.append(i)

print(diviseur)