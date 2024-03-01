def math():
    print("started")
    for i in range(20):
        x = yield i
        print(x)


d = math()
print(next(d))
print(d.send(6))
# .send method inheritances next and also sends the value to the stopped place. See examples.
#d.send(None) starts the decorator 

"""
The send() method controls what the value to the left of the yield expression will be.

To understand how yield differs and what value it holds, lets first quickly refresh on the order python code is evaluated.

Section 6.15 Evaluation order

Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is evaluated before the left-hand side.

So an expression a = b the right hand side is evaluated first.

As the following demonstrates that a[p('left')] = p('right') the right hand side is evaluated first.

>>> def p(side):
...     print(side)
...     return 0
... 
>>> a[p('left')] = p('right')
right
left
>>> 
>>> 
>>> [p('left'), p('right')]
left
right
[0, 0]
What does yield do?, yield, suspends execution of the function and returns to the caller, and resumes execution at the same place it left off prior to suspending.

Where exactly is execution suspended? You might have guessed it already... the execution is suspended between the right and left side of the yield expression. So new_val = yield old_val the execution is halted at the = sign, and the value on the right (which is before suspending, and is also the value returned to the caller) may be something different then the value on the left (which is the value being assigned after resuming execution).

yield yields 2 values, one to the right and another to the left.

How do you control the value to the left hand side of the yield expression? via the .send() method.

6.2.9. Yield expressions

The value of the yield expression after resuming depends on the method which resumed the execution. If __next__() is used (typically via either a for or the next() builtin) then the result is None. Otherwise, if send() is used, then the result will be the value passed in to that method.
"""