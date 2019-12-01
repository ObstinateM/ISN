from tkinter import *
f = Tk()
f.geometry('600x600+400+150')


# Variables globales

LC = [[0,0,0],[0,0,0],[0,0,0]]
joueur= 1

can = Canvas(f,bg="white",heigh=600,width=600)
can.pack()

can.create_line(200,0,200,600,width=2)
can.create_line(400,0,400,600,width=2)
can.create_line(0,200,600,200,width=2)
can.create_line(0,400,600,400,width=2)

def clic(event):
    global LC, joueur
    abs = event.x
    ord = event.y
    ligne = ord//200
    col = abs//200
    if LC[ligne][col]==0:
        if joueur==1:
            texte=can.create_text(col*200+100,ligne*200+100,text="O",font="Helvetica 120 bold",fill='blue')
            LC[ligne][col]=1
            joueur= 3-joueur
        elif joueur==2:
            texte=can.create_text(col*200+100,ligne*200+100,text="X",font="Helvetica 120 bold",fill='red')
            joueur= 3-joueur
            LC[ligne][col]=2
        print(LC)









can.bind('<Button-1>',clic)

f.mainloop()