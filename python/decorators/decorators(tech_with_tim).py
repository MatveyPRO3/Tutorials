import time

def timer(func):
    def wrapper():
        # start  = time.time()
        # val = func()
        # result  = time.time() - start 
        # print(result)
        # return val 
        print("hqhqh")
    return wrapper

@timer
def f():
    for i in range(9999999):
        pass
    print("f")
@timer
def f2():
    time.sleep(2)
    print("f2")
f()
f2()