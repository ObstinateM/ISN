# coding : utf8

ListeCarre = []
Resultat = []
i = 0
temp = 0
j = 0
l = 0
k = True

while k:
    var = input("Entrer un nombre (s pour stop) :")
    if var == "s":
        k = False
        l -= 1
    else:
        var = int(var)
        print(var)
        ListeCarre.append(var)
        l += 1
        print(ListeCarre)

while i <= l:
    temp = ListeCarre[i]
    temp = temp ** 2
    Resultat.append(temp)
    i += 1

print(Resultat)
