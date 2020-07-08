def collatz(n):  #defining collatz series	
	while n>1:
		if n%2 ==0:
			n=n//2
			#n=int(n)
			print(f"{n}")
		elif n%2 ==1:
			n=3*n +1
			print(f"{n}")

x= int(input("Enter Number:\n"))
collatz(x)