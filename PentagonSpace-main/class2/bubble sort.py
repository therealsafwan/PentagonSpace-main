a=[]
n=int(input("enter the no.of the elemenets:"))
print("enter the elements:")

a=[int(input())for i in range(n)]
for j in range(n):

    for i in range(0,(n-2)+1,1):
        if a[i]<a[i+1]:
            a[i]=a[i]+a[i+1]
            a[i+1]= a[i]-a[i+1]
            a[i]=a[i]-a[i+1]
        print(a)
print("")






