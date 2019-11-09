def gcd(a,b):
    if (b>a): 
        if (a==0):
            return b
        return gcd(a, b%a)
    if (a>b):
        if (b==0):
            return a
        return gcd(b , a%b )	

x = eval(input("Enter first number : "))
y = eval(input("Enter second number : "))	
z = gcd(x , y)
print("GCD of the numbers : ",z)	

