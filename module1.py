L = []
L2 = []
L3 = []
L4 = []



def crepe(L):
    """

    """
    infini = True
    long = len(L)
    long -= 1
    m = 0
    while infini:
        print(L)
        a = input("Retourner a partir de quel rang ?")
        a = int(a)
        b = long - a
        while b != long+1:
            tempo = L[b]
            L2.append(tempo)
            b = b + 1
        print(L2)
        while m < a:
            temp = L[m]
            L2.append(temp)
            m = m + 1
        print(L2)
        #print(L, L2)
        #return(L, L2)


        #if L == L.sort():
        #   print("C'est gagné")
        #   infini = False
        #else:




