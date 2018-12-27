year = int(input("Enter year"))
year1 = year
count = 0
agle = []
pichle = []

while True:
	year += 1
	year1 -= 1
	if (year % 4 == 0) or (year % 400 == 0):
		agle.append(year)
		pichle.append(year1)
		count += 1
		if count == 3:
			break
print "Pichle 3 Leap Year :",pichle[0],pichle[1],pichle[2]
print "Agle 3 Leap Year :", agle[0],agle[1],agle[2]
