def Main():
    str="pentagon"
    return str
def Outer(Arg):
    print("inside outer")
    def inner():
        print("inside inner")
        ptr=Arg()
        ans=ptr.upper()

        print(ans)
    return inner
ref=Outer(Main)
ref()
