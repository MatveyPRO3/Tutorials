class Foo():
    def greeting(self):
        print("Hi!")
def add_atribute(self):
    self.z = 5

myclass = type("myclass",(Foo,),{"x":5,"y":5,"name":"matvey","add_atribute":add_atribute})
cl = myclass()
cl.greeting()
print(cl.x)
cl.add_atribute()
print(cl.z)
