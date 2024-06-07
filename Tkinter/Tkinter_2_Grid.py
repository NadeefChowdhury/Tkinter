from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello")
myLabel2 = Label(root, text="I am Nadeef")
myLabel3 = Label(root, text="                 ")


myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()