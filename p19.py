#concatenate two lists in the given order as tuple

l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
l3=tuple(zip(l1,l2))
print(l3)