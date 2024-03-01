class my_own_dataclass:
    def __init__(self, cls) -> None:
        self.cls = cls

    def __call__(self, *args, **kwargs):
        obj = self.cls()
        # print(obj.__annotations__)
        if len(args) > len(obj.__annotations__):
            raise TypeError(
                f"__init__ method takes {len(obj.__annotations__)} arguments but {len(args)} were given"
            )
        args += (None,) * (len(obj.__annotations__) - len(args))

        for i, j in zip(obj.__annotations__, args):
            obj.__annotations__[i] = j

        obj.__dict__ |= obj.__annotations__

        return obj


@my_own_dataclass
class cls:
    a: int
    b: str
    c: float
    # def __init__(self,l) -> None:
    #     self.l = l


A = cls(5, "f")

print(A.a, A.b, A.c)
# This is a simplified model, in reality dataclass is a function, and by default it
# overwrites __init__
