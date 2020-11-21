#Exercice. Étant donné un générateur g qui fournit la séquence : a, b, c, d, e, ...,
# construire un générateur g2 qui donne a, a, b, b, c, c, d, d, e, e, ...
# Généraliser pour la réplication non pas deux, mais un nombre arbitraire, paramétrable, de fois. Itérer l'original g dans g2.
# au départ fais un générateur qui genere les lettres a, b, c

# ensuite tu poursuis l'exo il te faut un gen2 qui appelle gen pour doubler les lettres , donc quand l'appelle a gen te sort a, gen 2 te sort a a

# ensuite faut ajouter un param pour que gen2 te sorte a a a si le param vaut 3

# il triplera ou quadruplera etc...en fonction de ce que tu lui passes
def g():
    list = ['a', 'b', 'c']
    for i in range(0, 4):
        print(list[i])

def g2():
    list = ['a', 'b', 'c']
    for i in range(0, 4):
        print(list[i])
        g()
g2()