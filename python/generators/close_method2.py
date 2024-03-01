def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while 1:
            try:
                value=(yield value)
            except  Exception as e:
                value = e
        print("h")
    except Exception as e:
        print(e,"<--- ERROR")
    except BaseException as e:
        print(e,"<-- ERROR")
    finally:
        print("Don't forget to clean up when 'next()' is called.")

gen = echo(1)
print(next(gen))
# Run it in IDLE
# I was so confused by this paradox but now it seems i found explanation
# When you are running code in IDE it terminates process when the last line has been excecuted
# It raises StopGeneratorError(this error is object of BaseException) which not displayed because it is hidden by IDE itself (maybe IDE hides all errors which occurred after finishing execution)
# And when you run it in IDLE it doesn't kill the process immediately 
#https://amir.rachum.com/blog/2017/03/03/generator-cleanup/