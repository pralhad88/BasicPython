input1=int(input("Input: "))
if input1==0:
	print("Kuch Nahi")
a=0
b=1
i=0
while i < input1:
	if a%2==0:
		print(a,end=' ')
	c=a+b
	a=b
	b=c
	i+=1
print("Output:")