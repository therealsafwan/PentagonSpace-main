def even(n):
    if n%2==0:
        print(n,end="")
a=[]

n=int(input("enter the no.of elements:"))
print("enter the elements")
a=[int(input()) for i in range(n)]
for i in a:
    even(i)

