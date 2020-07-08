from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("test it is")
root.grid()

def randnum(event):
	import random
	value =random.randint(1,10)
	print(value)
	updateDisplay(value)

def updateDisplay(myString):
	displayVariable.set(myString)


button_1 = Button(root, text="test")
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable)
displayLabel.pack()
root.mainloop()