a=[]
n=int(input("enter the no.of the elemenets:"))
print("enter the elements:")

a=[int(input())for i in range(n)]
x=int(input("enter the search elements:"))

count=0
for i in a:
    if i==x:
        count=count+1
if(count==0):
    print("not found")
else:
    print("found")
    print("total occurance=",count)