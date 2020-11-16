# Ecrire un programme en Python permettant d’afficher pour une chaine de caractères donnée,
# le nombre d’occurrences de chaque caractère dans la chaine. Exemple pour la chaine de caractère s = « itescia.fr » le programme doit afficher :
# Le caractère : ” i ” figure 2 fois dans la chaine s
# Le caractère : ” t ” figure 1 fois dans la chaine s
# Le caractère : ” e ” figure 1 fois dans la chaine s
# Le caractère : ” s ” figure 1 fois dans la chaine s
# Le caractère : ” c ” figure 1 fois dans la chaine s
# Le caractère : ” a ” figure 1 fois dans la chaine s
# Le caractère : ” . ” figure 1 fois dans la chaine s
# Le caractère : ” f ” figure 1 fois dans la chaine s
# Le caractère : ” r ” figure 1 fois dans la chaine s
from collections import Counter

mot = input("Entrer un Mot !")
info = Counter(mot)
for char, count in info.items():
       print('Le caractere {0} figure {1} fois'.format(char, count))