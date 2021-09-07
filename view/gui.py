import tkinter.messagebox
from tkinter import *

root = Tk()


# if __name__ == '__main__':

def clicked():
    # Label(root, text="Clicked").grid()
    tkinter.messagebox.showinfo(title="click", message="ciao")


# label widget and packing to the screen
myLabel = Label(root, text="hello") \
    .grid(row=0, column=0)
myLabel1 = Label(root, text="Insert") \
    .grid(row=1, column=0)
buttton = Button(root, text="click", command=clicked) \
    .grid(row=2, column=1)

root.mainloop()
