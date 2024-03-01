def gen():
    yield 'so far so good'
    try:
        yield 'yay'
    finally:
        yield 'bye'

g=gen()
print(next (g))
'so far so good'
print(next(g))
'yay'
print(g.throw(ValueError('too bad')))
'bye'
print(next(g))
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/
#explanation: when try and finally are used witgout except if in try block error takes place interpreter remembers the error and switches to the finally and when finally becomes done it throws remembered error