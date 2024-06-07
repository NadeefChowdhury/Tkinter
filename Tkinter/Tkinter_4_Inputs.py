from tkinter import *

root = Tk()
entry = Entry(root, width=50, fg='white', bg='blue', borderwidth=5)
entry.pack()
entry.insert(0, "Enter your name: ")
def myClick():
    myLabel = Label(root, text="Your name is "+entry.get())
    myLabel.pack()
    
myButton = Button(root, text="Enter your name",  padx=50, pady=20, command=myClick, fg='white', bg='blue', state=NORMAL)  #YOU CAN ADD STATE = DISABLED or NORMAL or ACTIVE
myButton.pack()

root.mainloop()