s={1,2,3,4,5,6}

# s.remove(7)
# if the element given is not present in set , it raises KeyError;

s.discard(7)
# it does not raise error it given element is not present in set

deleted_element = s.pop()
# it removes the element and returns that element.

print(deleted_element)
print(s)