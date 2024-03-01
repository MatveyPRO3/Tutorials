class myclass():
    def __init__(self) -> None:
        self.a = "a"
    def __eq__(self,o):
        # print(myclass())
        return "LOL"
        # print("LOL")
    def __str__(self):
        return "str method completed"
    def __repr__(self):
        print(98)
        return self.__str__()
class P:
    def __init__(self) -> None:
        self.b = "B"
        self.array = [1,2,3,4]
    def __getitem__(self,i):
        return self.array[i]
a = myclass()
v = P()
# # print(a == v)
# # print(a)
# a == v
# print(v[2])
a#try it in jupyter or in raw console 
