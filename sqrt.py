import math
from decimal import Decimal
x = int(input("please enter the number you want to start with:\n"))
for i in range(x,x+10):
    sqrt=math.sqrt(i)
    a = round(sqrt,3)
    print(f"sqrt of {i} is : {a}")
exit()



