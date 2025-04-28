def lenght(n):
    l=0
    while(n!=0):
        n=n//10
        l=l+1
    return l
n=int(input("enter the num:"))
l=lenght(n)
print(l)

def calculation(n,l):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+(r**l)
        n=n//10
    return sum
print(calculation(n,l))

sum=calculation(n,l)
print(sum)
if(sum==n):
    print("armstrong")
else:
    print("not a armstrong")