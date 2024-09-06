
a = [1, 2, 3, 4, 5]
a.append(6)  
b = a  # Both b and a refer to the same list

# Change the value of an item at a specific index in b
b[2] = 10  # Modify index 2 of b

print("a:", a)
print("b:", b)

#a and b share the same list object, so modifying the list through either reference affects the list as seen through both references.
