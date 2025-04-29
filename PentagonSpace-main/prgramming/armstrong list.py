def armstrong(n):
    n=0
    while(n!=0):
        n=n//10
        n=n+1
    return n



n = int(input("enter the no.of elements:"))
print("enter the elements")
a = [int(input()) for i in range(n)]

for i in a:
    print(i)

