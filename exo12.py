# 1) – Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher la table de multiplication de ce nombre.
# 2) – Améliorez le programme afin qu’il affiche les tables de multiplications de tous les nombres compris entre 1 et 9
# Debut 1)
# On demande à l'utilisateur de saisir un nombre
# n = int(input("Entrer un nombre !"))
# on fait une boucle for pour afficher 10 fois la multiplication de i*n
# for i in range(1, 11):
#    print(n, "x", i, "=", i*n)
# Fin 1)
# Debut 2)
n = 1
i = 10
while n < i:
    for y in range(11):
        print(y, "x", n, "=", y*n)
    n = n + 1
# Fin 2)