# remove all occurrences of a specific item from list
# using list comprehension
l=[1,2,3,4,5,2,6,2,2,2,]
print(l)
item_remove=2
l = [item for item in l if item!=item_remove]
print(l)