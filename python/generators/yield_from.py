# example 1 

def gen():
    for i  in range(10):
        yield i
l = [1,2,34,4,5,68,8,7,8,8,8,9,9,8,9]
def gen2():
    yield from l
for i in gen2():
    print(i) 

# example 2 

def yieldOnly():
    yield "A"
    yield "B"
    yield "C"

def yieldFrom():
    for _ in [1, 2, 3]:
        # yield from yieldOnly()
        for i in yieldOnly():
            yield i

test = yieldFrom()
for i in test:
    print(i)

# 'yield from iter' is short form of 'for i in iter: yield i '