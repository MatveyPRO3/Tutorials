# In python each function is a descriptor
class myclassmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func.__get__(owner, type(owner)) # Two variants of implementation
        return lambda *args, **kwargs: self.func(owner, *args, **kwargs)


class cls:
    var = 5

    @myclassmethod
    def f(class_, g):
        class_.var += 1
        print(class_)


c = cls()
c.f(7)

a2 = cls()
print(a2.var)
print(a2.__dict__)

