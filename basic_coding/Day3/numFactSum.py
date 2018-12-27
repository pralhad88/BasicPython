x=input("Input: ")
sum1=0
for i in range(len(x)):
	a=int(x[i])
	fact=1
	for j in range(1,a+1):
		fact=fact*j
	sum1=sum1+fact
print("Output:",sum1)