n=int(input("enter the no.of elements:"))
print("enter the elements")
a=[int(input()) for i in range(n)]
sum=0
for i in a:
    sum=sum+i
    print(sum)

