# Ecrire un programme en langage Python, permettant d’échanger le premier et le dernier caractère d’une chaine donnée.
def permutation(chaine):
    print(chaine)
    chaineCasse = [i for i in chaine]
    dernier = len(chaineCasse) - 1
    tampon = chaineCasse[dernier]

    chaineCasse[dernier] = chaineCasse[0]

    chaineCasse[0] = tampon
    print(chaineCasse)


permutation("langage")