from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("400x400")

#Create a canvas
canvas= Canvas(win, width= 400, height= 400)
canvas.pack()

#Load an image in the script
img= (Image.open("Images/Nadeef-casual.jpg"))

#Resize the Image using resize method
resized_image= img.resize((300,300), Image.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

win.mainloop()