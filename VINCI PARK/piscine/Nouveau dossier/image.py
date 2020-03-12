from tkinter import *

from PIL import Image, ImageTk

def incrementationBut():
    nbrBut.set(nbrBut.get() + 1)
    print(nbrBut.get())
    nbrButAffichage.set(nbrBut.get())



fen = Tk()

frame1 = Frame(fen).pack()
frame2 = Frame(fen).pack()


img = [Image.open('but.jpg'), Image.open('but2.jpg')]
imgs = [ImageTk.PhotoImage(image=img[0]), ImageTk.PhotoImage(image=img[1])]
labImage = Label(frame1, image=imgs[0])
labImage.pack()


nbrBut = IntVar()
nbrBut.set(0)
etatBut = 1


nbrButAffichage = StringVar()
nbrButAffichage.set("0")

labelAffichageBut = Label(frame2, textvariable=nbrButAffichage)
labelAffichageBut.pack()

bouton = Button(frame2, text="But", command=incrementationBut)
bouton.pack()

fen.mainloop()
