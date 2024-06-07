from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Images")

#button_quit = Button(root, text="Exit Program", command=root.quit)
#button_quit.pack()
path = 'Images/Nadeef-casual.jpg'
my_img = ImageTk.PhotoImage(Image.open(path))
my_label = Label(image=my_img).pack()

root.mainloop()