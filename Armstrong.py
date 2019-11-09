def digits ( x ):
	c = x
	sum = 0
	m=0
	for i in range(1,10):	    
	    c = int(c/10)
	    if(c!=0):    
	        m=m+1   
	c=x 
	m=m+1
	for j in range(1,10): 	    
	    b = c%10
	    c = int(c/10)  
	    d = pow(b,m)
	    sum = sum+d
	if(x==sum):
	    print("Given number is Armstrong number")
	else :
	   print("Given number is not Armstrong number")    
	
x = eval(input("Enter a number : "))
digits(x)	
