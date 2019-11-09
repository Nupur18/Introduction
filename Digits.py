def digits ( x ):
	c = x
	sum = 0
	for i in range(1,10):
	    b = c%10
	    c = int(c/10)
	    sum = sum+b
	return sum    

	

x = eval(input("Enter a number : "))
val = digits(x)	
print ("Sum of digits : ", val)