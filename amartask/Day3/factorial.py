# This programme solve the factorial of a particular number. i.e factorial of 5 is (1*2*3*4*5) = 120.

def fact(n)
	if n==1:
		return 1
	else:
		return n * fact(n-1)
print("Output:",fact(int(input("Input: "))))
