from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Windows")

def openwindow():
    top = Toplevel()
    top.title("Top window")
    label = Label(top, text="Hi").pack()
    button2 = Button(top, text="Close", command=top.destroy).pack()
button = Button(root, text="Click to open new window", command=openwindow).pack()


root.mainloop()