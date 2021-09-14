import tkinter.messagebox
import guiEntryProcess
from tkinter import *

root = Tk()


def clickedMain():
    guiEntryProcess.GuiEntryProcess()
    # root.destroy()


buttonSwap = Button(root, text="Enter a new app to kill", command=clickedMain)
buttonSwap.pack()

root.mainloop()
