def f():
    x = 0
    while 1:
        try:
            x = yield x
        except ZeroDivisionError:
            print("Generator reset")


gen = f()
gen.send(None)
for i in range(20):
    print(gen.send(i))
    gen.throw(ZeroDivisionError)
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/