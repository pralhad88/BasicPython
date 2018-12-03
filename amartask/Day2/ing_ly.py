oldstr = input("Enter string ")
#contact=''
if oldstr[-3:]=="ing":
	newstr = oldstr + "ly"
	print(newstr)
elif oldstr[-2:] == "ly":
	print(oldstr)
elif oldstr[-3:]!="ing":
	if oldstr[-1:]=="e":
		newstr = oldstr[:-1] + "ing"
		print(newstr)
	else:
		newstr = oldstr + "ing"
		print(newstr)