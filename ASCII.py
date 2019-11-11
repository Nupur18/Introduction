def char( x ) :
	p = x.isalpha()
	if (p==True):
		print("ASCII value of character is",ord(x))
	else :
		print("Character of ASCII value",x,"is",chr(int(x)))

x = (input("Enter a character or an integer : "))
char(x)
