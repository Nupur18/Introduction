n = eval(input("Enter the value of n : "))
sum = 0
for i in range (1,n+1):
	x = i/(i+1)
	sum = sum + x
print("Sum of series : ", sum)	