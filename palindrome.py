for i in range(1,1001):
	a=str(i)
	b=""
	for j in range(len(a)-1,-1,-1):
		b = b + a[j]
		if a == b:
			print i,"palindrome"
