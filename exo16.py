# Ecrire un programme en langage Python qui permet de parcourir et afficher les caractères d’une variable du type
# chaine de caractères. Exemple pour s = « Python » , le programme affiche les caractères : P y t h o n
mot = input("Entrer un Mot !")
motCasse = [i for i in mot]
print(motCasse)