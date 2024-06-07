from tkinter import *

root = Tk()
def myClick():
    myLabel = Label(root, text="The button was clicked")
    myLabel.pack()
    
myButton = Button(root, text="Click me",  padx=50, pady=20, command=myClick, fg='white', bg='blue', state=NORMAL)  #YOU CAN ADD STATE = DISABLED or NORMAL or ACTIVE
myButton.pack()

root.mainloop()