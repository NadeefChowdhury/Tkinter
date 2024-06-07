from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

frame = LabelFrame(root, text="Frame", padx=50, pady=50)
frame.pack(padx=100, pady=100)
button = Button(frame, text="Button", padx=5).grid(row=0, column=0)
button2 = Button(frame, text="Button", padx=5).grid(row=0, column=1)


root.mainloop()