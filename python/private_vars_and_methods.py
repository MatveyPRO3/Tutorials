class a:
    lol = "lol"
    __a = "oo"
    def __init__(slf) -> None:
        slf._a = "_a"
        slf.b = "b"
        slf.c = "c"
        slf.__a = "__a"

    def print__a(self):
        print(self.__a)

    def __repr__(self):
        return str(self)  # forever recursion
    def __private(self):
        print("Private mrthid called")
    def call_private(self):
        self.__private()

a.print__a(a)
c = a()
c.print__a()
print(a.lol)
print(c._a)
print(c.lol)
c.call_private()
c.__private()
# print(c.__a)
# print(vars())
# print(str(c))
