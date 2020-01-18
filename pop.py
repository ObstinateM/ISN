from tkinter import *

Liste = ['Test', 'Test 2', 'Test 3', 'Test 4']

def valide():
	"""var = saisie.get()
				print(var)
				Liste.append(var)
				print(Liste)"""
	var = saisie.get()




def rm():
	print(Liste)
	Liste.pop()
	print(Liste)

root = Tk()
root.geometry('500x500+700+0')
root['bg'] = 'bisque'

can = Canvas(root, width = 500, height = 500, bg = 'white')
can.pack()

saisie = StringVar()
Champ = Entry(root, textvariable = saisie, bg = 'grey', fg = 'black')
Champ.place(relx = 0.1, rely = 0.1)

nombre = StringVar()
Write = Entry(root, textvariable = nombre, bg = 'grey', fg = 'black')
Write.place(relx = 0.1, rely = 0.4)

Valider = Button(root, text = 'Valider', command = valide)
Valider.place(relx = 0.7, rely = 0.1)

BPop = Button(root, text = 'Pop', command = rm)
BPop.place(relx = 0.7, rely = 0.4)

root.mainloop()









