def mygen(num):
    for i in range(num):
        yield num+i
        
for i in mygen(9):
    print(i)