x=input("Enter number")
p=['!','?','.']
vovel=['A','I','O','E','U','a','i','o','e','u']
joint=''
for i in range(len(x)):
	if x[i] not in p:
		joint=joint+x[i]
joint=joint.split()

c=[]
v=[]
for k in range(len(joint)):
	a=joint[k]
	if (a[0] in vovel) and (a[len(a)-1] in vovel):
		c.append(a)	
	else:
		v.append(a)
print("NUMBER OF WORDS BEGINNING AND ENDING WITH A VOWEL =",len(c))

for j in range(len(v)):
	c.append(v[j])
#print(c) first apped start and end with vovel then consonant are stored in c list 
merg=''
for x in range(len(c)):
	merg=merg + c[x] + " "
print(merg)

