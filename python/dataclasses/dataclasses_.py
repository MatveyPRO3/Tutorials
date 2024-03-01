from dataclasses import dataclass,field,InitVar
from turtle import position
from random import uniform
from inspect import getsource

@dataclass
class Book:
    title: str
    author: str
    gen_desc: InitVar[bool]
    desc: str = None

    def __post_init__(self, gen_desc: str):
        print("post ini called. ",gen_desc)
        if gen_desc and self.desc is None:
            self.desc = "`%s` by %s" % (self.title, self.author)
            
book = Book("a","a","d")


@dataclass
class Person:
    name: str = "Matvey"
    age: int = 14
    position: list = field(default_factory=list)
    def __post_init__(self,a):
        a=9
        self.info = " ".join(map(str, self.__dict__.values()))
        if self.position == []:
            self.position = [uniform(0, 10),
                      uniform(0, 10),
                      uniform(0, 10)]  # x y z

matvey = Person(position=[1,11,1,1,2,1,1,1,1,.0,1,1,1,111,1,],a=5)
matvey.age
print(matvey.info)
print(matvey.position)

