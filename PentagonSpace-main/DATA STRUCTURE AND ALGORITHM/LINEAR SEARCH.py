n=int(input("enter the size of the elements:"))
print("enter the elements")
a=[int(input()) for i in range(n)]
x=int(input("enter the search elements:"))

count=0
for i in a:
    if i==x:
        count=count+1
print("the total number of occurance=",count)