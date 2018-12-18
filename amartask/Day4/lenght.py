# Take a input as string and strored each chracter in a list and find how many element is there in a list. 

x=input("Input: ")
connect="" # Without taking split function
list=[]
for i in x:
    connect+=i
    if i == " ":
       list.append(connect)
       connect = " "
print(len(list)+1) # added one because last element can't append in a list because of if condition 

x=len(x.split()) # with a split function.
print("Output:",x)
