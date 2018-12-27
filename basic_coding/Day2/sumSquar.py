x = int(input("enter number "))

sum1 = 0
sum2 = 0

for i in range(1,x+1):
	a = i**2
	sum1 = sum1 + a
	sum2 = sum2 + i

print(sum2**2 - sum1)
