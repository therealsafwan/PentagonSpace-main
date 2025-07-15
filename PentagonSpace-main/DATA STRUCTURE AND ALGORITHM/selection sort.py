n=int(input("enter the size of the list:"))
print("enter the values into the list")
a=[int(input()) for i in range(n)]
print("unsorted list is",a)

for i in range(0,n-2+1,1):
    for j in range(i+1,n-1+1,1):
        if(a[i]>a[j]):
            c=a[i]
            a[i]=a[j]
            a[j]=c

print("sorted list is:",a)