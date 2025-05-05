a=input("enter the string 1:")
b=input("enter the string 2:")
mark=0
if len(a)!=len(b):
    mark=1
else:
    for i in a:
        count1=0
        count2=0

for j in a:
    if i==j:
        count1=count1+1
for j in b:
    if i==j:
        count2=count2+1
if count1!=count2:
     mark=1

if mark == 0:
     print("anagram")
 else:
     print("not a anagram")

