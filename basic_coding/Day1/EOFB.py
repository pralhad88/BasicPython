Pichle_even = int(input("enter number"))
Pichle_even1 = Pichle_even - 1
agle_odd = Pichle_even + 1 
count = 0
even = []
odd = []
while True:
	if Pichle_even%2==0:
		Pichle_even = Pichle_even - 2
		even.append(Pichle_even)
		odd.append(agle_odd)
		agle_odd = agle_odd + 2
		count=count+1
		if count == 3:
			break
	else:
		even.append(Pichle_even1)
		Pichle_even1 = Pichle_even1 - 2
		Pichle_even = Pichle_even + 2
		odd.append(Pichle_even)
		count = count+1
		if count == 3:
			break
print "Pichle 3 even number : ", even[0],even[1],even[2]
print "Agle 3 odd number : ",odd[0],odd[1],odd[2]
