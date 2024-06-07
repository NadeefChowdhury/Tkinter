from tkinter import *
from PIL import ImageTk, Image
import os

images = os.listdir('Images')
print(images)

root = Tk()
root.title("Images")

#button_quit = Button(root, text="Exit Program", command=root.quit)
#button_quit.pack()

image_number = 0
path = 'Images/' + images[image_number]
img = ImageTk.PhotoImage(Image.open(path))
my_label = Label(image=img)
my_label.grid(row=0, column=0, columnspan=3)
print("Length of image list: "+str(len(images)))

statusText = "Image " + (str(image_number+1)) + " out of " + str(len(images))
status = Label(root, text=statusText, bd=1, relief=SUNKEN)


def back_():
    
    global images
    global image_number
    global number
    global back
    number = image_number-1
    print(number)
    
    global my_label
    global my_img
    
    image_number = image_number -1
    path_back = 'Images/' + images[number]
    my_img = ImageTk.PhotoImage(Image.open(path_back))
    print(path_back)
    my_label.grid_forget()
    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    if number == 0:
        back =  Button(root, text="Previous", state=DISABLED,fg="white", bg="blue", command=back_)
        back.grid(row=1, column=0)
    else:
        back =  Button(root, text="Previous", fg="white", bg="blue", command=back_)
        forward = Button(root, text="Next", fg="white", bg="red", command=forward_)
        back.grid(row=1, column=0)
        forward.grid(row=1, column=2)
    statusText = "Image " + (str(image_number+1)) + " out of " + str(len(images))
    status = Label(root, text=statusText, bd=1, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def forward_():
    
    global image_number
    global images
    global number
    global forward
    number = image_number+1
    print(number)
    
    global my_label
    global my_img
    
    image_number = image_number+1
    path_forward = 'Images/' + images[number]
    my_img = ImageTk.PhotoImage(Image.open(path_forward))
    print(path_forward)
    my_label.grid_forget()
    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    if number == (len(images)-1):
        forward =  Button(root, text="Next", fg="white", state=DISABLED,bg="red", command=forward_)
        forward.grid(row=1, column=2)
    else:
        back =  Button(root, text="Previous", fg="white", bg="blue", command=back_)
        forward = Button(root, text="Next", fg="white", bg="red", command=forward_)
        back.grid(row=1, column=0)
        forward.grid(row=1, column=2)
    statusText = "Image " + (str(image_number+1)) + " out of " + str(len(images))
    status = Label(root, text=statusText, bd=1, relief=SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
back =  Button(root, text="Previous", fg="white", bg="blue", command=back_, state=DISABLED)
forward = Button(root, text="Next", fg="white", bg="red", command=forward_)
back.grid(row=1, column=0)
forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()