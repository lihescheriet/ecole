# Ecrire un programme en Python qui permet de lister les chaines qui composent la liste l = [“laptop”, “iphone”, “tablet”] tout en indiquant la longueur de chaque chaine.
l = ['laptop', 'iphone', 'tablet']
i = 0
for i in range(len(l)):
    print(l[i], len(l[i]))