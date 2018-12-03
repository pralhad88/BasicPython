x=int(input("Enter number"))
for i in range(x):
	a=list(str(i))
	sum1=0
	for j in range(len(a)):
		b=int(a[j])**len(a)
		sum1=sum1+b
	if i==sum1:
		print(i,"amstrong")

