str=input("enter the sentence:")
str1=str.split()
rev=""
for i in str1:
    #rev=i+rev
    rev=i+" "+rev
print(rev)
