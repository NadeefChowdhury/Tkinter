from tkinter import *
from itertools import cycle
 
class App(Tk):
    def __init__(self, textList, master=None):
        Tk.__init__(self, master)
        self.textiter = cycle(textList)
        self.txt = StringVar()
        self.rootEntry = Entry(self, textvariable=self.txt)
        self.rootEntry.pack()
        self.rootEntry.bind("<Return>", self.cycle_text)
        self.rootText = Text(self)
        self.rootText.pack()
        self.rootText.bind("<Insert>", self.insert_all)
        self.newList = []
 
    def cycle_text(self, arg=None):
        t = self.textiter.next()
        self.txt.set(t)
        self.rootText.insert("end", t+"\n")
        self.newList.append(self.rootText.get("end - 2 chars linestart", "end - 1 chars"))
 
    def insert_all(self, arg):
        self.rootText.insert("end", "".join([s.strip() for s in self.newList]))
 
textList = ["Line 1", "Line 2", "Line 3"]
root = App(textList)
root.mainloop()