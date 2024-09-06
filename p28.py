# 18. Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.

def sort_strings(strings):
    l1=[i for i in strings if i.startswith('x')]
    l2=[i for i in strings if not i.startswith('x')]
    return sorted(l1)+sorted(l2)

l = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

print(sort_strings(l))