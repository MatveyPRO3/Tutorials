global_a = "global_a"
global_b = "global_b"


def change_global_a():
    global global_a
    global_a = "Changed_global_a"


x = "global"


def outer():
    global x
    x = "local"

    def inner():
        # nonlocal x

        # Interepreter thinks that here is only the second layer because outside this func x defined as global
        # and it is no difference between it selected as global by outer func or it created via standart way on the first layer
        
        x = "nonlocal"
        # print("inner:", x)

    inner()
    print("outer:", x)


change_global_a()

print(global_a, global_b)
print(":::::::::::::::::::::::")
outer()
print(x)
