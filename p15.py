# Turn every item to list to it's square
l=[1,2,3,4,5,6,7]
print(l)
for i in range (1,len(l)):
    l[i]=l[i]**2
print(l)