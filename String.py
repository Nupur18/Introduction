def upper(x):
	for i in p :
		if (i!=" "):
			a = ord(i) - 32
			b = chr(a)
			print(b,end="")
		if (i==" "):
			print(" ",end="")
		
p = input("Enter a string in lowercase : ")
upper(p)





