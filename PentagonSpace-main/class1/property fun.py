class car:
    def __init__(self):
        self.__brand=""
    def getter(self):
        return self.__brand
    def setter(self,value):
        self.__brand=value
    getset=property(getter,setter)
c1=car()
c1.getset="BMW"
res=c1.getset
print(res)


