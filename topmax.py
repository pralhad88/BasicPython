x=[86,10,1,23,41,54,45]
max1=0
max2=0
max3=0
for i in x:
	if i > max1:
		max1=i
	elif i>max2:
		max2=i
	elif i>max3:
		max3=i
print max1,max2,max3


	##ORIGINAL STEP
x=[86,10,1,23,41,54,45]
max1=0
for i in x:
	if i > max1:
		max1=i
max2=0
for i in x:
	if i > max2 and  i!=max1:
		max2=i
max3=0
for i in x:
	if i > max3 and i!=max1 and i!=max2:
		max3=i 
print max1,max2,max3
