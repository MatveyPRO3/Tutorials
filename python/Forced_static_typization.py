def static_types(func):
    def wrapper(*args,**kwargs):
        print(func.__annotations__)
        for i,j in zip(func.__annotations__.values(), args):
            if not isinstance(j,i):
                raise TypeError
        print(args,kwargs)
    return wrapper

@static_types
def f(a:int):
    print(a)
    
f(5)
    