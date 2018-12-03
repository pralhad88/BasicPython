x=input("Enter any  world ")
y= input("Enter seond world ")
if len(x)==len(y):
	for i in range(len(x)):
		if y[i] not in x:
			print("nahi hai")
			break
	print ("hai")

else:
	print ("Nahi hai")