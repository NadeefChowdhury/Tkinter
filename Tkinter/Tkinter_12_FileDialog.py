from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Frame")



def open_():
    global my_img
    global my_label
    root.filename = filedialog.askopenfilename(initialdir="Images", title="Select a file", filetypes=(("all files", "*.*"),("png files", ".png"),("jpg files", ".jpg")))
    myLabel = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(image=my_img).pack()    


button = Button(root, text="Open Image", command=open_).pack()


root.mainloop()