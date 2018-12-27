for number in range(1001):
	string=list(str(number))
	
	sum_of_each_digit=0
	for j in range(len(string)):
		int_number=int(string[j])
		power_of_digit = int_number ** len(string)
		sum_of_each_digit += power_of_digit
	
	if number == sum_of_each_digit:
		print (number, "Is amstrong Number")
