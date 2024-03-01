class geometric_figure():
    def __init__(self, *args, **kwargs) -> None:
        self.__dict__.update(kwargs)
        self.__dict__.update(args)
        self.public = "public"
        self.__private = "private"

    def area(self):
        return self.width*self.height
        # return "he he it is a main parent"

    def high_level_function(self):
        print("LOL")


class rectangle(geometric_figure):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


class square(rectangle):
    def __init__(self, a) -> None:
        super(square, self).__init__(a, a)

    def area(self):
        return "Not working"


class cube(square):
    def __init__(self, a) -> None:
        super(cube, self).__init__(a)

    def volume(self):
        if (s := self.area()) == "Not working":
            # the second parament is an object of class given at first place
            # we need second parameter to for placing it in a method as self
            # if there wasn't be second parameter in super we will must call super like super(rectangle).area(self)
            # Example: I had a cube object and i need an old version of method that will change my object i can only use super or geometric_figure.area(self)

            s = geometric_figure.area(self)  # the same variants
            s = super(rectangle, self).area()

        h = self.height
        return h*s


class something():
    def __init__(self) -> None:
        self.width = 1
        self.height = 1
        print(super(rectangle, cube(5)).area())
        # or
        # print(cube(5).area())


square1 = square(5)
print(square1.area())

cube1 = cube(7)
print(cube1.area())
print(cube1.volume())
# We had inherited all methods even from the highest class
cube1.high_level_function()
print(isinstance(cube1, geometric_figure))

somebody1 = something()

# https://realpython.com/python-super/#super-in-multiple-inheritance
