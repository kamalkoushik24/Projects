#made by kamal koushik duppalapudi
#Housie
from random import randint
import time
for draw in range(90):
 done=list()
 num=randint(1,90)
 if not num in done:
  print(num)
  done.append(num)

  # c=input("Do you want to check  for any number?")
  # if c == "n" or c == "N":
  #   continue
  # if c not in ["n","N","Y","y"]:
  #  print("sorry please type y or n")
  # elif c == "Y" or c == "y":
  #    while True:
  #     j = int(input("Which number do you want to check for ?\n"))
  #     if j in done:
  #      print("done")
  #     elif j not in done and j != 0:
  #      print("not done yet")
  #     elif j == 0:
  #      break
