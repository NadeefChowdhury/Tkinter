from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Message Box")

def popup():
    messagebox.showinfo("This is my Popup", "Hello world")  #YOU CAN USE showerror, showwarning, askquestion, askyesno, askcancel etc

def popup2():
    response = messagebox.askyesno("This is my Popup", "Hello")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="YESSSSS").pack()
    if response == 0:
        Label(root, text="Noooooo").pack()
    

Button(root, text="Popup Info", command=popup).pack()
Button(root, text="Popup Yes-No", command=popup2).pack()

root.mainloop()