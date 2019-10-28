L =[]
L1 =[]
def retourne_jusque(L,k):
    A =-1
    B =len(L)
    B1 = B-k
    print(B)
    while k!=A :
        L1.append(L[k])
        k = k-1
        print(L1)
        while B1 !=B :
            L1.append(L[B1])
            B = B+1
            print (L1)