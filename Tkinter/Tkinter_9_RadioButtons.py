from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio")

#r = IntVar()
def clicked(value):
    global myLabel
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion")
    
    ]

pizza = StringVar()
pizza.set("Pepperoni")
for text, mode in MODES:
    Radiobutton(root, text=text, value=mode, variable=pizza,  command=lambda:clicked(pizza.get())).pack()


myLabel = Label(root, text=pizza.get())
myLabel.pack()


root.mainloop()