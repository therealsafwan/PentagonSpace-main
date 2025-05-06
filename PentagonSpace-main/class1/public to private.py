class Dog:
    def __init__(self):
        self.name="chintu"

    def __Bark(self):
        print("chintu is barking")

    def helper(self):
        self.__Bark()
d1=Dog()
print(d1.name)
d1.helper()
