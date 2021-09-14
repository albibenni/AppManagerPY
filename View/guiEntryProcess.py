# windows conditions * check for .exe spelling


import tkinter.messagebox
from tkinter import *


class GuiEntryProcess:
    root = Tk()
    e = Entry(root, width=50)
    e.pack()

    def __init__(self):
        buttonEntry = Button(self.root, text="Enter the process name", command=self.clicked)
        buttonEntry.pack()
        self.root.mainloop()

    def clicked(self):
        processName = self.e.get()
        if processName[-4:] != ".exe":
            processName = processName + ".exe"
        # call to the kill function or the return function to the main gui
        tkinter.messagebox.showinfo(title=processName, message=f"{processName} won't disturb you anymore")
        self.root.destroy()



GuiEntryProcess()
