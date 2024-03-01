def f():
    while 1:
        yield "g"


gen = f()
print(next(gen))
print(next(gen))
print(next(gen))
gen.close()
# print(next(gen))
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/