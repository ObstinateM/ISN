#1) Créer une fonction qui prend en argument un nombre x et
#qui affiche 2x²-3x+2

def lecrack(x):
    var = 2 * (x**2) - 2 * x + 2
    print(var)

#2) Créer une fonction qui prend en argument 2 nombres a et b
#et affiche le plus grand des deux

def grand(a, b):
    if a > b:
        print(a)
    else:
        print(b)

#3) Créer une fonction qui prend en argument3 nombres a, b et c
#et les affiche dans l'ordre croissant

def croissant(ListeCroissante):
    ListeCroissante.sort()
    print(ListeCroissante)

#4) Créer une fonction qui prend une liste de nombres en
#argument et affiche le max de cette liste

def maximum(Liste):
    long = len(Liste)
    long -= 1
    Liste.sort()
    print(Liste[long])

#5) Créer une fonction qui prend en argument un entier et
#affiche la liste de ses diviseurs


def diviseur(y):
    i = 1
    ListeDiviseur = []
    while i <= 100:
        temp = y % i
        if temp == 0:
            ListeDiviseur.append(i)
        else:
            pass
        i += 1
    print(ListeDiviseur)














