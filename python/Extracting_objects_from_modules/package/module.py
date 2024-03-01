import __main__


def f():
    if hasattr(__main__, "update"):
        __main__.update()
    if hasattr(__main__, "animate"):
        __main__.animate()
    if hasattr(__main__, "var"):
        print(__main__.var)
