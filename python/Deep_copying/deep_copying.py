from copy import deepcopy

lst1 = [1, 2, 3, [1, 2, 3]]
lst2 = deepcopy(lst1)
# # lst2 = lst1.copy()

# # lst1[3].append(5)
# # print(lst1,lst2)
print(id(lst1[0]) == id(lst2[0])) # int - simple object, cant be changed
print(id(lst1[3]) == id(lst2[3])) # list - complex object, can be changed
# # print(f"{lst1} - {id(lst1)}",f"{lst2} - {id(lst2)}",id(lst1) == id(lst2),sep="\n")

# deepcopy creates another list but elements of this list is links to the source list. If element is mutable it dublicates fully else link to that element is created 