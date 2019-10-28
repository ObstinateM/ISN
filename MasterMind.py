
k = 0
Liste = ['0','1','2','3']
ListeJoueur = []
test = True

def jeu(ListeJoueur):
    global Liste
    i = 0
    cptbon = 0
    cptpasbon = 0
    while i < len(Liste):
        print(Liste[i], ListeJoueur[i])
        if ListeJoueur[i] == Liste[i]:
            cptbon += 1
        else:
            cptpasbon += 1
        i += 1
    print(cptbon, cptpasbon)
    return(cptbon, cptpasbon)
    ListeJoueur.clear()

while test:
    texte = "Les nombres bon sont : " + str(cptbon)
    pourlaliste = input(texte)
    print(pourlaliste, k)
    while k < len(pourlaliste):
        var = pourlaliste[k]
        print(var)
        ListeJoueur.append(var)
        k = k + 1
    print(ListeJoueur)
    jeu(ListeJoueur)
    if ListeJoueur == Liste:
        print("C'est gagné")
        infini = False
    else:
        pass









