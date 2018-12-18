number = int(input("Number = "))
power = int(input("Power = "))
answer = str(number**power)

sum1=0
for i in range(len(answer)):
	sum1 = sum1 + int(answer[i])

print("Output:",sum1)
