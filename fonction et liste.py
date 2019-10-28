L = []
L2 = []
L3 = []
L4 = []
L5 = []
k = 0

def retourne(L):
    a = len(L)
    a -= 1
    while a >= 0:
        L2.append(L[a])
        a -= 1
    return(L2)

def echange_avec(L3, k):
    premierrang = L3[0]
    rangk = L3[k-1]
    L3[k-1] = premierrang
    L3[0] = rangk
    return(L3)

def retourne_jusque(L4, l):
    long = len(L4)
    long -= 1
    m = 0
    l -= 1
    while long >= l:
        L5.append(L4[long])
        long -= 1
    while m != l:
        L5.append(L4[m])
        m += 1
    return(L5)

def listediv(y):
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
     
L6 = []
L7 = []
L8 = []
     
def intersect(L6, L7):
    i = len(L6)
    k = len(L7)
    n = 0
    print("i :", i, "k : ", k, "n :", n)
    while n <= i:
        elt = L6[n-1]
        print(elt)
        if elt in L7:
            L8.append(elt)
        else:
            pass
        n += 1
    return L8
    
    
    








