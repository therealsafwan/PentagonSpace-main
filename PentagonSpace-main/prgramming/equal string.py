a=input("enter the string 1:")
b=input("enter the string 2:")
mark=0
if len(a)!=len(b):
    mark=1
else:
    for i in range (len(a)):
        if(a[i]!=b[i]):
            mark=1
if (mark==0):
    print("equal")
else:
    print("not equal")