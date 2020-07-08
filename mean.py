n = int(input("For how many values you want the mean for ?: "))
v=[]
for i in range(1,n+1):
 x=float(input(f"Value {i} : "))
 v.append(x)
 mean=sum(v)/n

print(f"Mean of the given values is :{mean}")
