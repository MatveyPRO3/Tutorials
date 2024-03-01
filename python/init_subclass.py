class A:
    def __init_subclass__(cls, arg1, arg2) -> None:
        print("A", arg1, arg2)
    q = 0


class A2:
    def __init_subclass__(cls, arg1, arg2, arg3) -> None:
        print("A2", arg1, arg2, arg3)


class a(A2, A, arg1=1, arg2=2, arg3=5):
    pass


print(a.q)
# child(subclass) can be initialized only once, but nevertheless it can inherit
# from multiple parents
# Arguments, are used only for subclass-initialization, this means they
# will be ignored after it.
# In above example a inherits from A and A2 but because of the left to right
# execution order in python A2 receives a permission to initialize it as his
# subclass and use its arguments, after this, arguments cannot be used for
# smth else
# Important! Code inside class is executed before init_subclass method in
# parent class (here is an example:https://stackoverflow.com/questions/45400284/understanding-init-subclass)
