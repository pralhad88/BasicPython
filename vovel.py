x=raw_input("enter name")
a=["a","i","o","u","e",'A','E','I','O','U']
y=[]
p=""
for i in range(len(x)):
	if x[i] in a:
		print x[i]
		y.append('*')
	else:
		y.append(x[i])
s=""
for j in range(len(y)):
	s=s+y[j]
print s

