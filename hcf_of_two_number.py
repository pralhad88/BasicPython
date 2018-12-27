def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

print (hcf(120, 100))