class decorator:
    def __init__(self,arg) -> None:
        self.arg = arg
    def __call__(self, *args, **kwargs):
        if type(*args) != str and type(*args) != int:
            def wrapper(a):

                print("recieved function")
                for i in range(self.arg):
                    retval = args[0](a)
                print("it was successfully done")
                return retval

            return wrapper
        else:
            print("start")
            val = self.arg(*args,**kwargs)
            print("end")
            return val
            
    def mycall(iters):
        
        def dec(func):
            def wrapper(*args,**kwargs):
                print(iters)
                print("s")
                val = func(*args,**kwargs)
                print("e")
                return val
            return wrapper
        return dec

@decorator.mycall(10)
def function(a):
    print(a)
    return 4
function("gggg")
print(function("9"))

print("-----------------------------------------")

@decorator(2)
def function2(a):
    print(a)
    return 4
function2("ffff")
print(function2("10"))
