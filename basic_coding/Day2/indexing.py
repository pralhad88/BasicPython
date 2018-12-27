x = input("Enter any string ")
if len(x) == 1:
	print("Empty")
else:
	conect = ''
	for i in range(len(x)):
		conect = conect + x[i]
		if i == 1:
			break
	conect = conect + x[len(x)-2] + x[len(x)-1]
	print(conect)
