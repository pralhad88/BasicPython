x=int(input("Enter number"))
box48, box24, box12, box6 = 48, 24, 12, 6 
if x>1000:
	print("Invalid Lenght")
	exit()
if x%48!=0:
	a1=int(x/48)
	b=a1*48
	print(box48,"x",a1,"=", b)
	c=x-b
if c%24!=0:
	a2=int(c/24)
	b=a2*24
	print(box24,"x",a2,"=", b)
	c=c-b
if c%12!=0:
	a3=int(c/12)
	b=a3*12
	print(box12,"x",a3,"=", b)
	c=c-b
if c%6!=0:
	a4=int(c/6)
	b=a4*6
	print(box6,"x",a4,"=", b)
	c=c-b
	print("Remaining boxes", c,"x 1 =", c*1)
	print("Total number of box =",x)
	print("Total number of carton =",a1+a2+a3+a4+1)
elif c%6==0:
	a4=int(c/6)
	b=a4*6
	print(box6,"x",a4,"=", b)
	c=c-b
	print("Remaining boxes",c,"x 0 =", c*1)
	print("Total number of box =",x)
	print("Total number of carton =",a1+a2+a3+a4)