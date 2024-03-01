a = b = 3
#   |
#   |
#  \|/
tmp = 3
a = tmp
b = tmp


def tricky_example():
    a, b = a[b] = a = [1, 2, 3], 2
    tmp = [1, 2, 3], 2
    a, b = tmp  # a=[1,2,3] b=2
    a[b] = tmp  # a = [1,2,(...)] b=2
    a = tmp  # a '=' [a,b] '=' [[1,2,(...)],2]
    print(a, b, tmp)
    print(a)
    print(b)
    print(tmp)


tricky_example()
