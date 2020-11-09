# Ecrire un programme en Python qui demande à l’utilisateur de saisir 3 nombre x, y et z et de lui afficher leur maximum
nb1 = int(input("Entrer un Nombre"))
nb2 = int(input("Entrer in Deuxieme Nombre "))
nb3 = int(input("ENtrer un dernier Nombre "))
if nb1 > nb2 and nb1 > nb3:
    print(nb1)
elif nb2 > nb1 and nb2 > nb3:
    print(nb2)
elif nb3 > nb1 and nb3 > nb2:
    print(nb3)

