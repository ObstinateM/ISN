ListeNote = []

k = True
i = 0
total = 0
var = 0

while k:
    var = input("Entrer un nombre (s pour stop) :")
    if var == "s":
        k = False
        i -= 1
    else:
        var = float(var)
        ListeNote.append(var)
        total += var
        i += 1

ListeNote.sort()
moyenne = total / i


print("La moyenne : ",moyenne)
print("La note minimale est : ", ListeNote[0], "La note maximale est :", ListeNote[i])
print("La liste des notes : ", ListeNote)

