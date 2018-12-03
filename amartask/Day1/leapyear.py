year=int(input("Enter year"))
if (year%4==0 and year%400!=0) and (year%100==0):
	print("leap year nahi hai")
elif (year%4==0) or (year%400==0):
	print("leap year hai")
else:
	print("leap year nahi hai")