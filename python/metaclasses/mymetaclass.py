class mymetaclass(type):

    def __init__(self):
        print("init called")

    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = attrs
        a["c"] = 4
        a["__init__"] = self.__init__
        return type(class_name, bases, a)


class Dog(metaclass=mymetaclass):
    a = 0
    b = 0

    def hello(self):
        print("hello!")
        print(self.c)

print(type(Dog))
# mydog = Dog()
# mydog.hello()
