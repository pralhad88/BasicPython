#     Decimal to Binary conversion

number = input('please enter the no. in decimal format: ')
x = number
list1=[]
while (number > 0):
    a=int(number % 2)
    list1.append(a)
    number = (number - a) / 2
list1.append(0)

string = ""
for j in range(len(list1)-1,-1,-1):
    string = string + str(list1[j])

print 'The binary no. for',x, 'is',string

#  Binary to Decimal conversion

binary_number = raw_input("please enter the number in binary format: ")
list2 = []
for i in range(len(binary_number)-1,-1,-1):
	list2.append(binary_number[i])

decimal_num = 0
for j in range(len(list2)):
	if int(list2[j]) == 1:
		power_of_lenght = 2**j
		decimal_num = decimal_num + power_of_lenght
print "Decimal number is",decimal_num
		
