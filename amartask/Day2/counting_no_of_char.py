l=raw_input("Enter any name here:-  \n")
l1=[]
for i in l:
	if i in l1:
		continue
	else:
		l1.append(i)
		print i,"is",l.count(i),"time"