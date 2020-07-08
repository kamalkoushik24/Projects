import random
from tkinter import *
x=random.random()

root = Tk()

w = Label(root, text=x)
w.pack()

root.mainloop()