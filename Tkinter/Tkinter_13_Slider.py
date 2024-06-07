from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider")
root.geometry("400x400")

def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()+400)+"x"+str(vertical.get()+400))
    
horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()     ###HERE .pack() MUST BE IN A SEPARATE LINE

vertical = Scale(root, from_=0, to=200)
vertical.pack()
    
button = Button(root, text="Click", command=slide).pack()

root.mainloop()