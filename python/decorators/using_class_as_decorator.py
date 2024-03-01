
# Full example version with accompanying doc string


class Power():
    def __init__(self, arg):
        self._arg = arg
        print("initialized", self._arg)

    def __call__(self, *param_arg):
        """If there are decorator arguments, __call__() is only called once
        as part of the decoration process. You can only give it a single argument,
        which is the function object
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        if len(param_arg) == 1:
            def wrapper(a, b):
                retval = param_arg[0](a, b)
                return retval ** self._arg
            return wrapper
        else:
            expo = 2
            retval = self._arg(param_arg[0], param_arg[1])
            return retval ** expo


@Power(3)
def multiply_together(a, b):
    return a * b


print(multiply_together(2, 2))
