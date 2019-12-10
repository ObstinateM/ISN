from tkinter import *

fenetre = Tk()
fenetre.geometry('750x750+0+50')
fenetre.title('Le titre de la fenetre')
fenetre['bg'] = 'black'

Bleu = Canvas(fenetre, bg = 'white', width = 1000, height = 1000, cursor = 'pirate')
Bleu.create_oval(10,10,750,750, fill = 'black', activefill = 'orange')
Bleu.create_rectangle(250,275,350,450, fill = 'blue')
Bleu.create_rectangle(350,275,450,450, fill = 'white')
Bleu.create_rectangle(450,275,550,450, fill = 'red')
Bleu.create_text(400, 500, text = 'DRAAPEAUUUU FRANCAAAIIIIS', fill = 'black', activefill = 'orange', font = 'Arial 24 bold')
#Bleu.create_oval(10,10,750,750, fill = 'black', activefill = 'orange')
Bleu.pack()




fenetre.mainloop()

