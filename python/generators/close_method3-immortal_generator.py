def immortal_generator():
    while 1 :
        try:
            yield "You cannot kill me "
        except BaseException:
            print("Nice try")

gen  = immortal_generator()
print(next(gen))
print(gen.close())
# print(next(gen))
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/