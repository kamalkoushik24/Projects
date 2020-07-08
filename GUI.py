from random import randint
from time import sleep
import tkinter as tk
h = 640
w = 480
root = tk.Tk()
root.title("Housie Number Generator")
def take():
        done = list()
        num = randint(1, 90)
        if not num in done:
            ran=str(num)
            num1 = canvas.create_text(240,320, font='Sans 40 bold', text=ran)
            root.update()
            done.append(num)
            sleep(2)
            canvas.delete(num1)
canvas = tk.Canvas(root, height=h, width=w, bg='#8ba3c6')
canvas.place(relheight=1, relwidth=1)

button = tk.Button(root, text="Generate", bg='gray', fg='black', command=take)
button.place(x=240,y=60)

root.mainloop()
