def f():
    print(7)
    yield 1, 23, 4
    print("ll")
    yield 1
    print("l")
    yield 7


gen = f()
print(9)
print(next(gen))
print(gen.close())
print(next(gen))
