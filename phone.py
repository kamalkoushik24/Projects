#!/usr/bin/env python3

import os
import csv
import django
def clear():
   if os.name == 'posix':
      _ = os.system('clear')

file = open("phone.csv", "a")
while True:
 person = input("Name of the person:")
 if person == "":
  clear()
  break
 num = input("Phone number:")

 r = csv.writer(file)
 r.writerow((person , num))
