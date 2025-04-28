str=input("enter the string:")
print(str)

if str.isalpha():
    print("contains only alphabetes")

elif str.isdigit():
    print("contains only digit")

elif str.isalnum():
    print("contains both")

else:
    print("contains some other character")