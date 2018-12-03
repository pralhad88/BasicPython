# If you want cheack only one number is perfect or not
x=int(input("Enter number"))
sum1=0
for i in range(1,x):
	if x%i==0:
		print(i)
		sum1=sum1+i
#print(sum1)
if sum1==x:
	print(x,"perfect number hai")

# If you want to cheak multiple number is perfect number is or not.
x=int(input("Enter number"))
for i in range(1,x):
	sum2=0
	for j in range(1,i):
		if i%j==0:
			sum2=sum2+j
	if sum2==i:
		print(i,"Is Perfect Number")
