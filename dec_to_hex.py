number = input('please enter the no. in decimal format: ')
x = number
remainder = []
list1=[]
while (number > 0):
    a=int(number % 16)
    remainder.append(a)
    number = (number - a )/16

for i in range(len(remainder)):
	if remainder[i] == 10:
		list1.append('A')
	elif remainder[i] == 11:
		list1.append('B')
	elif remainder[i] == 12:
		list1.append('C')
	elif remainder[i] == 13:
		list1.append('D')
	elif  remainder[i] == 14:
		list1.append('E')
	elif remainder[i] == 15:
		list1.append('F')
	else:
		list1.append(remainder[i])

string = ""
for j in range(len(remainder)-1,-1,-1):
    string = string + str(list1[j])
print 'The Hexadecimal number of', x, 'is',string

