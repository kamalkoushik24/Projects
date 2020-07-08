while True:
  s = input("Do you agree?\n")
  if s[0]in ["y", "Y"]:
   print("agreed")
   break
  elif s[0] in ["n", "N"]:
   print("not agreed")
   break
  elif s == "exit" or s == "quit":
   exit()
