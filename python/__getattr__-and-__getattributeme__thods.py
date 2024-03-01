

class Count:
    def __init__(self, mymin, mymax):
        self.mymin = mymin
        self.mymax = mymax

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0

    def __getattribute__(self, item):

        # print(type(item))
        # if item.startswith('cur'):
        # print("h")
        print("smth")
        return object.__getattribute__(self, item)


obj1 = Count(1, 10)
print(obj1.mymin)       # 1
print(obj1.mymax)       # 10
print(obj1.current1)  # 0
print(getattr(obj1, "mymin"))
"""
Each time when you're accessing object variable __getattribute__ method is called this method calls object.__getattribute__
method which scanning object variables, and if it can't find specified variable returns None than 
__getattribute__ raises an error if __getattr__ isn't implemented.
"""
# My model         / \
#                   |
#                   |
#
#                   |
#                   |
# Correct variant  \ /


"""
Python access to object attribute actions order:
1. __getattribute__ method called
2. if attribute is a data descriptor it is called (descriptor with set or delete method)
3. checking object __dict__
4. checking class __dict__
5. raise AttributeError -> __getattr__ method called 

Going through these steps until one of them will return something or will be implemented 
"""
