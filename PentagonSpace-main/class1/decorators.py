def Main():
    print("this is main")
def Outer(Arg):
    print("inside outer")
    def inner():
        print("entering inner")
        ptr=Arg
        ptr()
        print("leaving inner")
    return inner
ref=Outer(Main)
ref()
