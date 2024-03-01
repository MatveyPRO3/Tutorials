def decoraator(func):
    def wrapper(*args,**kwargs):
        print("s")
        func(*args,**kwargs)
        print("e")
    return wrapper

@decoraator
def f1(text):
    print(text)
print(f1)
print(f1("uuuuu"))