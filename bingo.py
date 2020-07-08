#libraries to import

#randint generates a random integer
from random import randint
#tkinter for GUI windows
from tkinter import *
#time is here so that sleep can be used to cause a wait between draws
import time

#Create Bingo GUI window
root=Tk()
#title for Window
root.title("Bingo")
#stops users resizing window
root.resizable(0,0)
#puts window at front
root.wm_attributes("-topmost",1)

canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
root.update()

def bingo(self):
 canvas.delete(title_screen)
 canvas.delete(title_text)
 root.update_idletasks()
 root.update()
#Bingo in the UK uses the numbers 1 to 90
for draw in range(90):
#as numbers are generated they are added to a list to stop duplication
 drawn_numbers=list()
#generates a random integer between 1 and 90
 bingo_draw=randint(1,90)
#if the number is already in the list it is discarded
 if not bingo_draw in drawn_numbers:
  bingo_str=str(bingo_draw)
  current_number = canvas.create_text(250,250,font='Times 80 bold',text=bingo_str)
  root.update()
#append to add the number to the list
  drawn_numbers.append(bingo_draw)
#wait inbetween each draw
  time.sleep(10)
  canvas.delete(current_number)

title_screen=canvas.create_text(250,50,font='Times 40 bold',text="BINGO")
title_text=canvas.create_text(250,200,font='Times 40 bold',text="Press space to Start")
canvas.bind_all('<Key-space>', bingo)
root.update_idletasks()
root.update()