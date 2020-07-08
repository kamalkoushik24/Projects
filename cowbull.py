import os
from time import sleep
import math
from random import randint
def clear():
   if os.name == 'posix':
      _ = os.system('clear')
p = int(input("please give a random number for guessing:\n"))
x = int(input("please enter the number of chances you want to get:\n"))
sleep(0.1)
clear()
y = int(input("please guess the number:\n"))
for  i in range(0,x):
  y = int(input("please guess the number:\n"))
  if y != p :
    print(f"you have {x-i-1} chances left")
  if i == x-1 :
    print("you were not able to guess the number correctly, please try next time")
    continue

  if y == p:
    print("yay! you have guessed the number correctly!!")
    break


print("yay! you have guessed the number correctly!!")
