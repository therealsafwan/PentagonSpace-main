class student:
    def __init__(self):
        self.__=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value

s1=student()
s1.dataAccess="safwan"
res=s1.dataAccess
print(res)
