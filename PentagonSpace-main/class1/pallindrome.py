n=int(input("enter the num:"))
copy=n
rev=0
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10
    rev=rev+r

if(copy==rev):
    print("palindrome")
else:
    print("not a palindrome")