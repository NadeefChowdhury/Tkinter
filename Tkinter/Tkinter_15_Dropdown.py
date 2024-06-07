from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown")
root.geometry("400x400")


options = [
    "Meow", "Gheu", "Panda"
    ]

clicked = StringVar()
clicked.set(options[0])
def show():
    myLabel = Label(root, text=clicked.get()).pack()
    

drop = OptionMenu(root, clicked, *options)
drop.pack()
button = Button(root, text="Show", command=show).pack()

root.mainloop()