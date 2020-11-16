def chiffrePorteBonheur(nb):
    # permet de déterminer si un nombre entier est chiffre porte bonheur ou non
    # un nombre chiffre porte Bonheur est un nombre entier, qui lorsqu'on ajoute les carrés de chacun de
    # ses chiffres puis les carrés des chiffre de ce resultat et ainsi de suite jusqu'a l'obtention d'un
    # nombre à un seul chiffre égal à 1
    # le calcule s'arrête lorsque le chiffre devient inférieur à 10
    # je dois prendre chacun de ces  chiffre est pour faire ça je dois diviser par 100, 10, etc
    # 64 du coup sa fait  6**2 + 4 ** 2 = 36 + 16 = 52 du coup on fait 5 ** 2 + 2 ** 2 = 25 + 4 = 29 du coup 2 ** 2 + 9 ** 2 = 4 + 81 = 85 ainsi de suite jusqua arriver en dessous de 10
    centaine = 0
    dizaine = 0
    mille = 0
    sums = 0
    if nb > 1000:
        mille = int(nb / 1000)
        nb -= (mille * 1000)
    if nb > 100:
        centaine = int(nb / 100)
        nb -= (centaine * 100)
    if nb > 10:
        dizaine = int(nb / 10)
        nb -= (dizaine * 10)

    print(mille, centaine, dizaine, nb)
    sqMille = mille ** 2
    print("le carre de ", mille, "est ", sqMille)
    sqCentaine = centaine ** 2
    print("le carre de ", centaine, "est ", sqCentaine)
    sqDizaine = dizaine ** 2
    print("le carre de ", dizaine, "est ", sqDizaine)
    sqNb = nb ** 2
    print("le carre de ", nb, "est ", sqNb)

    sums += sqMille + sqCentaine + sqDizaine + sqNb
    print(sums)
    if 10 < sums:
        # tant que sums n'est pas en dessous de 10 on continue ainsi de suite 
        while sums > 10:
            var = sums

            mille = 0
            centaine = 0

            if var > 1000:
                mille = int(var / 1000)
                var -= (mille * 1000)
                print("le millier est ", mille)
            if var > 100:
                centaine = int(var / 100)
                var -= (centaine * 100)
                print("la centaine est ", centaine)
            if var > 10:
                dizaine = int(var / 10)
                uniter = var - (dizaine * 10)
                print("la dizaine est ", dizaine)
                print("l'uniter est ", uniter)
            sqvarMille = mille ** 2
            print("le carre de ", mille, "est ", sqvarMille)
            sqvarCen = centaine ** 2
            print("le carre de ", centaine, "est ", sqvarCen)
            sqvarDiz = dizaine ** 2
            print("le carre de ", dizaine, "est ", sqvarDiz)
            sqvarUniter = uniter ** 2
            print("le carre de ", uniter, "est ", sqvarUniter)
            sums = sqvarMille + sqvarCen + sqvarDiz + sqvarUniter
            print(sums)






# execution
chiffrePorteBonheur(64)

