from tkinter import *
from tkinter.messagebox import *
from random import *
Liste = ['0','1','2','3','4','5','6','7','8','9']
ListeGagnante = []
shuffle(Liste)
for i in range(0,4):
	var = Liste[i]
	ListeGagnante.append(var)
print(ListeGagnante) # Debug

def jeu():
	global ListeGagnante
	UneListe = laliste.get()
	UneListe = list(UneListe)
	i = 0
	cptbon = 0
	if ListeGagnante == UneListe:
		showinfo('Reponse', 'Gagné félicitation !')
		fenetre.destroy()
	else:
		while i < len(UneListe):
			if UneListe[i] == ListeGagnante[i]:
				cptbon += 1
				i += 1
			else:
				i += 1
	Text.set(str(cptbon) + ' chiffre(s) est/sont à la bonne place.')
	laliste.set('')
	print(cptbon, " chiffre(s) est/sont à la bonne place.")

def indice():
	global ListeGagnante
	i = randint(0,3)
	print('i =', i)
	indice = ListeGagnante[i]
	textelocal = 'Indice : ' + str(indice) + ' (' + str(i+1) + ' ème position)'
	IndiceText.set(textelocal)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.geometry('550x100+400+400')
fenetre.title('MasterMind 2')
fenetre['bg'] = 'white'

Text = StringVar()
Texte1 = Label(fenetre, textvariable = Text, fg = 'red')
Texte1.pack(side = TOP, padx = 5, pady = 5, fill = BOTH)

IndiceText = StringVar()
TexteDeIndice = Label(fenetre, textvariable = IndiceText, fg = 'red')
TexteDeIndice.pack(side = TOP, padx = 5, pady = 5, fill = BOTH)

Texte2 = Label(fenetre, text = 'Entre 4 chiffres :')
Texte2.pack(side = LEFT, padx = 5, pady = 5, fill = BOTH)

laliste = StringVar()
Champ = Entry(fenetre, textvariable = laliste, bg = 'grey', fg = 'black')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5, expand = TRUE)

Bouton = Button(fenetre, text ='Valider', command = jeu)
Bouton.pack(side = LEFT, padx = 5, pady = 5, fill = X)

bouton_indice = Button(fenetre, text ='Indice', command = indice)
bouton_indice.pack(side = LEFT, padx = 5, pady = 5, fill = X)

bouton_quitter = Button(fenetre, text = 'Quit', command = fenetre.destroy)
bouton_quitter.pack(side = LEFT, padx = 5, pady = 5, fill = X)

fenetre.mainloop()