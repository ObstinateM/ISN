from random import randint

Boucle = True
i = 0

ListeJoursFrancais = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
ListeJoursAnglais = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

i = randint(0,6)

while Boucle:
    rep = input("Donne " + str(ListeJoursFrancais[i]) + " en anglais : ")
    rep = rep.lower()
    if rep == ListeJoursAnglais[i]:
        print("Correct")
        Boucle = False
    else:
        print("Faux")