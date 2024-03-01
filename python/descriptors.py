class B: # data-descriptor
    def __init__(self) -> None: # called first of all when descriptor is initialized
        print("init")
    def __set_name__(self, obj, name):  # called at first when descriptor assigned to prop
        print("__set_name__ method called")
        print(self, obj, name)
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        print("__get__ method called")
        print(obj,objtype)
        return getattr(obj, self.name)

    def __set__(self, obj, val):
        print("__set__ method called")
        print(self, obj, val)
        setattr(obj, self.name, val)


class X:
    a = 1
    b = B()
    c = B()

    def __init__(self):
        self.b = 2
        self.c = 3


x = X()
x.b = 9
print(x.a, x.b, x.c, x.__dict__, X.__dict__)


"""
Python access to object attribute actions order:
1. __getattribute__ method called
2. if attribute is a data descriptor it is called (descriptor with set or delete method)
3. checking object __dict__
4. checking class __dict__
5. raise AttributeError -> __getattr__ method called 

Going through these steps until one of them will return something or will be implemented 
"""

#ALL FUNCTIONS IN PYTHON ARE DESCRIPTORS!!!!!!!!!1