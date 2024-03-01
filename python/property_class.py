class property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
        self._name = ''

    def __set_name__(self, owner, name):
        print("setname called")
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError(f'unreadable attribute {self._name}')
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError(f"can't set attribute {self._name}")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError(f"can't delete attribute {self._name}")
        self.fdel(obj)

    def getter(self, fget):
        prop = type(self)(fget, self.fset, self.fdel, self.__doc__)
        prop._name = self._name
        return prop

    def setter(self, fset):
        prop = type(self)(self.fget, fset, self.fdel, self.__doc__)
        prop._name = self._name
        return prop

    def deleter(self, fdel):
        prop = type(self)(self.fget, self.fset, fdel, self.__doc__)
        prop._name = self._name
        return prop

class Number:

    def __init__(self, number):
        self.__number = number

    @property
    def nb(self):
        print("Getting...")
        return self.__number
    # def temp():pass 
    # nb = property(temp)

    @nb.setter
    def nb(self, number):
        print("Setting...")
        self.__number = number
    # def temp():pass
    # nb = nb.setter(temp)

    @nb.deleter
    def nb(self):
        print("Deleting...")
        del self.__number

    # nb = property()
    # nb = nb.getter(get_number)
    # nb = nb.setter(set_number)
    # nb = nb.deleter(del_number)


n = Number(42)

print(n.nb)
n.nb = 69
print(n.nb)
del n.nb
print(n.nb)

"""
Python access to object attribute actions order:
1. __getattribute__ method called
2. if attribute is a data descriptor it is called (descriptor with set or delete method)
3. checking object __dict__
4. checking class __dict__
5. raise AttributeError -> __getattr__ method called 

Going through these steps until one of them will return something or will be implemented  
"""

# property is a descriptor under the hood
