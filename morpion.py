from tkinter import *
 
pair = 0
place = 0

# Définition des variables pour check la win
Rond_Colonne_1 = 0
Rond_Colonne_2 = 0
Rond_Colonne_3 = 0
Rond_Ligne_1 = 0
Rond_Ligne_2 = 0
Rond_Ligne_3 = 0
Rond_Diagonale_1 = 0
Rond_Diagonale_2 = 0

Croix_Colonne_1 = 0
Croix_Colonne_2 = 0
Croix_Colonne_3 = 0
Croix_Ligne_1 = 0
Croix_Ligne_2 = 0
Croix_Ligne_3 = 0
Croix_Diagonale_1 = 0
Croix_Diagonale_2 = 0

egalite = 0
gagne = True

 
# Definition des fonctions
def clic(event):
    """Fonction qui prend en parametre les elements renvoyez par le clic. Place un rond ou une croix au centre de la case ou le joueur a clique. Modifie le texte a X de jouer. Compte le nombre de rond/croix
    par ligne et colonne. Au bout de 3 affiche le message gagné.
    """
    global pair, gagne, place, Rond_Colonne_1, Rond_Colonne_2, Rond_Colonne_3, Rond_Ligne_1, Rond_Ligne_2, Rond_Ligne_3, Rond_Diagonale_1, Rond_Diagonale_2, Croix_Colonne_1, Croix_Colonne_2, Croix_Colonne_3, Croix_Ligne_1, Croix_Ligne_2, Croix_Ligne_3, Croix_Diagonale_1, Croix_Diagonale_2, egalite
    colonne = event.x // 200
    ligne = event.y // 200
    #print("Colonne = ", colonne, "Ligne = ", ligne)
    coord_x = 200 * colonne + 100
    coord_y = 200 * ligne + 100
    #print("Ligne : ", ligne)
    egalite += 1
    print(egalite)
    if pair % 2 == 0:
        place = Can.create_text(coord_x, coord_y, text = 'O', font = 'Arial 96 bold', fill = 'blue')

        if colonne == 0:
        	Rond_Colonne_1 += 1
        elif colonne == 1:
        	Rond_Colonne_2 += 1
        elif colonne == 2:
        	Rond_Colonne_3 += 1

        if ligne == 0:
        	Rond_Ligne_1 += 1
        elif ligne == 1:
        	Rond_Ligne_2 += 1
        elif ligne == 2:
        	Rond_Ligne_3 += 1

        if ligne == 0 and colonne == 0:
        	Rond_Diagonale_1 += 1
        elif ligne == 1 and colonne == 1:
        	Rond_Diagonale_1 += 1
        elif ligne == 2 and colonne == 2:
        	Rond_Diagonale_1 += 1

        if ligne == 0 and colonne == 2:
            Rond_Diagonale_2 += 1
        elif ligne == 1 and colonne == 1:
            Rond_Diagonale_2 += 1
        elif ligne == 2 and colonne == 0:
            Rond_Diagonale_2 += 1

        if Rond_Colonne_1 == 3 or Rond_Colonne_2 == 3 or Rond_Colonne_3 == 3 or Rond_Ligne_1 == 3 or Rond_Ligne_2 == 3 or Rond_Ligne_3 == 3 or Rond_Diagonale_1 == 3 or Rond_Diagonale_2 == 3:
            Can.create_text(300, 175, text = 'Les ronds ont gagnés !', font = 'Arial 20 bold')
            Can.unbind('<Button-1>')
            gagne = False

        pair += 1
        joueur.set('C\'est au Croix de jouer.')

    else:
        place = Can.create_text(coord_x, coord_y, text = 'X', font = 'Arial 96 bold', fill = 'red')

        if colonne == 0:
        	Croix_Colonne_1 += 1
        elif colonne == 1:
        	Croix_Colonne_2 += 1
        elif colonne == 2:
        	Croix_Colonne_3 += 1

        if ligne == 0:
        	Croix_Ligne_1 += 1
        elif ligne == 1:
        	Croix_Ligne_2 += 1
        elif ligne == 2:
        	Croix_Ligne_3 += 1

        if ligne == 0 and colonne == 0:
            Croix_Diagonale_1 += 1
        elif ligne == 1 and colonne == 1:
            Croix_Diagonale_1 += 1
        elif ligne == 2 and colonne == 2:
            Croix_Diagonale_1 += 1

        if ligne == 0 and colonne == 2:
            Croix_Diagonale_2 += 1
        elif ligne == 1 and colonne == 1:
            Croix_Diagonale_2 += 1
        elif ligne == 2 and colonne == 0:
            Croix_Diagonale_2 += 1

        if Croix_Colonne_1 == 3 or Croix_Colonne_2 == 3 or Croix_Colonne_3 == 3 or Croix_Ligne_1 == 3 or Croix_Ligne_2 == 3 or Croix_Ligne_3 == 3 or Croix_Diagonale_1 == 3 or Croix_Diagonale_2 == 3:
            Can.create_text(300, 175, text = 'Les croix ont gagnés !', font = 'Arial 20 bold')
            gagne = False
            Can.unbind('<Button-1>')

        pair += 1
        joueur.set('C\'est au Rond de jouer.')

    if egalite == 9:
        Can.create_text(300, 175, text = 'Egalite !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>') 

def cancel():
	"""Fonction qui annule le coup.
	"""
	global pair
	Can.delete(place)
	pair -= 1
	joueur.set('Recommencer votre coup.')

def reset():
    """Fonction qui détruit et recreer le canvas pour reset la grille. Reset les variables.
    """
    global Can, pair, place, Rond_Colonne_1, Rond_Colonne_2, Rond_Colonne_3, Rond_Ligne_1, Rond_Ligne_2, Rond_Ligne_3, Rond_Diagonale_1, Rond_Diagonale_2, Croix_Colonne_1, Croix_Colonne_2, Croix_Colonne_3, Croix_Ligne_1, Croix_Ligne_2, Croix_Ligne_3, Croix_Diagonale_1, Croix_Diagonale_2, egalite
    pair = 0
    Can.destroy()
    Can = Canvas(root, width = 600, height = 600, bg = 'white')
    Can.create_line(200, 0, 200, 600, fill = 'black')
    Can.create_line(400, 0, 400, 600, fill = 'black')
    Can.create_line(0, 200, 600, 200, fill = 'black')
    Can.create_line(0, 400, 600, 400, fill = 'black')
    Can.pack()
    Can.bind('<Button-1>', clic)
    joueur.set('C\'est au Rond de jouer.')
    Rond_Colonne_1 = 0
    Rond_Colonne_2 = 0
    Rond_Colonne_3 = 0
    Rond_Ligne_1 = 0
    Rond_Ligne_2 = 0
    Rond_Ligne_3 = 0
    Rond_Diagonale_1 = 0
    Rond_Diagonale_2 = 0
    Croix_Colonne_1 = 0
    Croix_Colonne_2 = 0
    Croix_Colonne_3 = 0
    Croix_Ligne_1 = 0
    Croix_Ligne_2 = 0
    Croix_Ligne_3 = 0
    Croix_Diagonale_1 = 0
    Croix_Diagonale_2 = 0
    egalite = 0
 
# Fenetre principale
root = Tk()
root.title('Morpion')
root.geometry('600x700')
root['bg'] = 'black'
 
# Zone de dessin
Can = Canvas(root, width = 600, height = 600, bg = 'white')
 
# Ligne et colonne
#place = Can.create_text(300, 300, text = 'Appuie sur RESET pour commencer la partie')
Can.create_line(200, 0, 200, 600, fill = 'black')
Can.create_line(400, 0, 400, 600, fill = 'black')
Can.create_line(0, 200, 600, 200, fill = 'black')
Can.create_line(0, 400, 600, 400, fill = 'black')
Can.pack()

Quitter = Button(root, text = 'Quitter', command = root.destroy)
Quitter.pack(side = BOTTOM)
 
Cancel = Button(root, text = 'Annuler le dernier coup', command = cancel)
Cancel.pack(side = BOTTOM)

Reset = Button(root, text = 'Reset', command = reset)
Reset.pack(side = BOTTOM)

joueur = StringVar()
joueur.set('C\'est au Rond de jouer.')
Texte = Label(root, textvariable = joueur, font = 'Helvetica 16 italic', fg = 'red', bg = 'black')
Texte.pack(side = BOTTOM)

# Bind des fonctions
Can.bind('<Button-1>', clic)
 
root.mainloop()