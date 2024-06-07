from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider")
root.geometry("400x400")

var = StringVar()
def show():
    myLabel = Label(root, text=var.get()).pack()
c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off",command=show)
c.deselect()
c.pack()


root.mainloop()