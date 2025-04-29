def reverse(n):
    rev=0
    while(n!=0):
        r=n%10
        n=n/10
        rev=rev*10
        rev=rev+n
    print(rev)

a=[]

n=int(input("enter the no.of elements:"))

a=[int(input()) for i in range(n)]
for i in a:
    reverse(i)

