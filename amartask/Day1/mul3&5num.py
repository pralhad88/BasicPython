x = int(input("Enter number"))
for i in range(1,x+1):
	if i % 3 == 0 or i % 5 == 0:
		print(i,end=' ')
print()
