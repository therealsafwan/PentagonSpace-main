a=input("enter the string 1:")
b=input("enter the string 2:")
mark=0
if len(a)!=len(b):
    mark=1
else:
    for i in a:
        if(a.count(i)!=b.count(i)):
            mark=1
if (mark==0):
    print("anagram")
else:
    print("not a anagram")