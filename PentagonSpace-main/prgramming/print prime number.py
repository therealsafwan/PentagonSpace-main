def prime(n):
    count=0
    for i in range (1,n+1,1):
        if n%2==0:
            count=count+1
        if count==2:
         print(n)
a=[]

n=int(input("enter the no.of elements:"))
print("enter the elements")
a=[int(input()) for i in range(n)]
for i in a:
    prime(i)

