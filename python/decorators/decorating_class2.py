class Decorator(object):
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, cls):
        class Wrapped(cls):
            classattr = self.arg
            def new_method(self, value):
                return value * 2
        return Wrapped

@Decorator("decorated class")
class TestClass(object):
    def new_method(self, value):
        return value * 3

a = TestClass()# We created object of class Wrapped
print(a.new_method("j "))