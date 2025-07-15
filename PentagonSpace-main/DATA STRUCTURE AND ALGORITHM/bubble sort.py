n=int(input("enter the size of the list:"))
print("enter the values into the list")
a=[int(input()) for i in range(n)]
print("unsorted list is",a)

for j in range(0,n,1):
    for i in range(0,n-2+1,1):
        if(a[i]>a[i+1]):
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
print("sorted list is",a)
