class bird():
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print("Hello")

    def create_new_var(self, **new_var):
        self.__dict__.update(new_var)

    def print_var(self, var):
        print(self.__dict__[var])


class dog():
    def __init__(self, name) -> None:
        self.name = name

    def say_gaf(self):
        print("gaf")

    def print_var(self, var):
        print(self.__dict__[var])


Parrot = bird("Trinky")
Parrot.print_var("name")
Parrot.create_new_var(age=67)
Parrot.print_var("age")
Taksa = dog("Gaf")
bird.create_new_var(Taksa, age=89)
Taksa.print_var("age")
