n=int(input("enter the size of the elements:"))
print("enter the elements")
a=[int(input()) for i in range(n)]
x=int(input("enter the search elements:"))

i=0
j=n-1
mark=0

while(i<=j):
    mid=(i+j)//2
    if x==a[mid]:
        print("element found")
        mark=1
        break

    elif x>a[mid]:
        i=mid+1
    else:
        j=mid-1

if mark==0:
    print("element not found")
