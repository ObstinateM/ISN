import random
L = [1,2,3,4,5,6,7,8]
#L = [3,4,2,5,6,1,8,7]
random.shuffle(L)
print(L)
ListeDeVerification = []
ListeDeVerification = L.copy()
ListeDeVerification.sort(reverse=True)
#L = [3,4,2,5,6,1,8,7]
# <-- Bas / Haut -->

infini = True

def retourne(k):
    global L
    Liste2 = []
    k = int(k)
    l = k - 1
    m = len(L)
    i = 0
    # Boucle pour ajouter les nombres entre 0 et k dans la Liste2
    while l > -1:
        temporairedeliste = L[l]
        Liste2.append(temporairedeliste)
        l = l - 1
    k = k + 1
    while k <= m:
        temporaire_de_la_liste_2 = L[k-1]
        Liste2.append(temporaire_de_la_liste_2)
        k = k + 1
    L = Liste2.copy()
    #print(L, Liste2) # Debug
    return(L)

while infini:
    texte = "La liste est :" + str(L) + " \nDonne le rang de retournement"
    var = input(texte)
    var = int(var)
    retourne(var)
    if L == ListeDeVerification:
        print("C'est gagné")
        infini = False
    else:
        pass











