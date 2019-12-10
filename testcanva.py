from tkinter import *
root = Tk()

listeOptions = ('train', 'avion', 'bateau')
v = StringVar()
v.set(listeOptions[0])
om = OptionMenu(root, v, *listeOptions)
om.pack()

root.mainloop()