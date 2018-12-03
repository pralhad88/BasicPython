x=input("Input: ")
contact=''
a=[]
for i in range(len(x)-1,-1,-1):
	if x[len(x)-1]=="0":
		if x[i] == "0":
			a.append(x[i])
		else:
			contact=contact+x[i]
	else:
		contact=contact+x[i]
print(contact)

def reverse_number(fac):
    r = 0
    while fac > 0:
        r = r * 10
        r = r + fac % 10
        fac = fac // 10
    return r

fac=int(input())
k=reverse_number(fac)
print (k)

