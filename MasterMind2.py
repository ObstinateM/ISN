from random import shuffle
Liste = ['0','1','2','3','4','5','6','7','8','9']
ListeGagnante = []
shuffle(Liste)
for i in range(0,4):
	var = Liste[i]
	ListeGagnante.append(var)
print(ListeGagnante) # Debug
inf = True
nbcoup = 0

def jeu(UneListe):
	global ListeGagnante
	i = 0
	cptbon = 0
	while i < len(UneListe):
		if UneListe[i] == ListeGagnante[i]:
			cptbon += 1
			i += 1
		else:
			i += 1
	print(cptbon, " chiffre(s) est/sont à la bonne place.")

while inf:
	entree = list(input("Entre une liste de nombre : "))
	if entree == ListeGagnante:
		nbcoup += 1
		print("Gagné ! La liste était :" + str(ListeGagnante) + " (en " + str(nbcoup) + " coups)")
		inf = False
	else:
		jeu(entree)
		nbcoup += 1