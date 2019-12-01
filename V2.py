L = [3,1,5,4,2,6,7,8]
#    3,1,2,4,5

infini = True
long = len(L)



def renverser(k):
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    global L
    i = 0
    while i < k-1:
        temp = L[i]
        L2.append(temp)
        i = i + 1
    a = len(L2)
    a -= 1
    while a >= 0:
        L3.append(L2[a])
        a -= 1
    while k <= long:
        temp2 = L[k-1]
        L4.append(temp2)
        k = k + 1
    L5 = L4 + L3
    L = L5
    return(L, L2, L3, L4, L5)
    print(L, L2, L3, L4, L5)

"""
while infini:
    texte = "La liste est :" + str(L) + "  Donne un nombre"
    k = input(texte)
    k = int(k)
    renverser(k)
    if L == L.sort():
        print("C'est gagné")
        infini = False
    else:
        pass
"""