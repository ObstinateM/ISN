from tkinter import *
 
pair = 0
place = 0
colonne = 0
ligne = 0

# Définition des variables pour check la win
ListeCoup = []
Liste = [[0,0,0],[0,0,0],[0,0,0]]
egalite = 0
gagne = True

# Definition des fonctions
def clic(event):
    """Fonction qui prend en parametre les elements renvoyez par le clic. Place un rond ou une croix au centre de la case ou le joueur a clique. Modifie le texte a X de jouer. Compte le nombre de rond/croix
    par ligne et colonne. Au bout de 3 affiche le message gagné.
    """
    global pair, place, egalite, ligne, colonne, gagne
    colonne = event.x // 200
    ligne = event.y // 200
    coord_x = 200 * colonne + 100
    coord_y = 200 * ligne + 100
    egalite += 1
    if Liste[ligne][colonne] == 0:
        if pair % 2 == 0:
            place = Can.create_text(coord_x, coord_y, text = 'O', font = 'Arial 96 bold', fill = 'blue')
            Liste[ligne][colonne] = 1
            pair += 1
            joueur.set('C\'est aux Croix de jouer !')
        else:
            place = Can.create_text(coord_x, coord_y, text = 'X', font = 'Arial 96 bold', fill = 'red')
            Liste[ligne][colonne] = 2
            pair += 1
            joueur.set('C\'est aux Ronds de jouer !')
    ListeCoup.append(place)
    print(Liste)

    # Rond
    # Colonne
    for i in range(0,3):
        if(Liste[i][0]==Liste[i][1]==Liste[i][2]==1):
            Can.create_text(300, 175, text = 'Les ronds ont gagnés !', font = 'Arial 20 bold')
            Can.unbind('<Button-1>')
            gagne = False

    # Lignes    
    for i in range(0,3):
        if(Liste[0][i]==Liste[1][i]==Liste[2][i]==1):
            Can.create_text(300, 175, text = 'Les ronds ont gagnés !', font = 'Arial 20 bold')
            Can.unbind('<Button-1>')
            gagne = False

    # Diagonales
    if(Liste[0][0]==Liste[1][1]==Liste[2][2]==1):
        Can.create_text(300, 175, text = 'Les ronds ont gagnés !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>')
        gagne = False

    if(Liste[0][2]==Liste[1][1]==Liste[2][0]==1):
        Can.create_text(300, 175, text = 'Les ronds ont gagnés !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>')
        gagne = False


    # Croix
    # Colonne
    for i in range(0,3):
        if(Liste[i][0]==Liste[i][1]==Liste[i][2]==2):
            Can.create_text(300, 175, text = 'Les croix ont gagnées !', font = 'Arial 20 bold')
            Can.unbind('<Button-1>')
            gagne = False

    #lignes    
    for i in range(0,3):
        if(Liste[0][i]==Liste[1][i]==Liste[2][i]==2):
            Can.create_text(300, 175, text = 'Les croix ont gagnées !', font = 'Arial 20 bold')
            Can.unbind('<Button-1>')
            gagne = False

    #diagonales
    if(Liste[0][0]==Liste[1][1]==Liste[2][2]==2):
        Can.create_text(300, 175, text = 'Les croix ont gagnées !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>')
        gagne = False

    if(Liste[0][2]==Liste[1][1]==Liste[2][0]==2):
        Can.create_text(300, 175, text = 'Les croix ont gagnées !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>')
        gagne = False

    egalite = 9
    #vide
    for i in range(0,3):
        for j in range(0,3):
            if(Liste[i][j]!=0):
                egalite -= 1
                #print(egalite)

    if egalite == 0 and gagne:
        Can.create_text(300, 175, text = 'Égalité !', font = 'Arial 20 bold')
        Can.unbind('<Button-1>')

def cancel():
    """Fonction qui annule le coup.
    """
    global pair, ListeCoup, colonne, ligne
    Can.delete(ListeCoup[-1])
    ListeCoup.pop(-1)
    Liste[ligne][colonne] = 0
    pair -= 1
    joueur.set('Recommencer votre coup.')
    #print("LISTE APRES : ", Liste)

def reset():
    """Fonction qui détruit et recreer le canvas pour reset la grille. Reset les variables.
    """
    global Can, pair, place, egalite, Liste, gagne
    pair = 0
    Can.destroy()
    Can = Canvas(root, width = 600, height = 600, bg = 'white')
    Can.create_line(200, 0, 200, 600, fill = 'black')
    Can.create_line(400, 0, 400, 600, fill = 'black')
    Can.create_line(0, 200, 600, 200, fill = 'black')
    Can.create_line(0, 400, 600, 400, fill = 'black')
    Can.pack()
    Can.bind('<Button-1>', clic)
    joueur.set('C\'est aux Ronds de jouer !')
    egalite = 0
    gagne = True
    #Liste.clear()
    Liste = [[0,0,0],[0,0,0],[0,0,0]]

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
 
Cancel = Button(root, text = 'Annuler le dernier coup  (Ne fonctionne pas : \n aucune idee pour annuler le dernier ajout dans une liste)', command = cancel)
Cancel.pack(side = BOTTOM)

Reset = Button(root, text = 'Reset', command = reset)
Reset.pack(side = BOTTOM)

joueur = StringVar()
joueur.set('C\'est aux Ronds de jouer !')
Texte = Label(root, textvariable = joueur, font = 'Helvetica 16 italic', fg = 'red', bg = 'black')
Texte.pack(side = BOTTOM)

# Bind des fonctions
Can.bind('<Button-1>', clic)
 
root.mainloop()