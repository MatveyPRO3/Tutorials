def decorator(decor_arg):

    class ClassWrapper:
        def __init__(self, cls):
            self.other_class = cls
            print("class wrapper initialized")

        def __call__(self, *cls_ars):
            other = self.other_class(*cls_ars)
            other.field += decor_arg
            return other

    return ClassWrapper


@decorator(" is now decorated.")
class NormalClass:
    def __init__(self, name):
        self.field = name

    def __repr__(self):
        return str(self.field)


A = NormalClass('A')
# B = NormalClass('B')

print (A)
# print (B)
print (NormalClass.__class__)
