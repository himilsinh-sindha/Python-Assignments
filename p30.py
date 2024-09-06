# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3].

def remove_duplicate_adjacents(l1):
    result = [l1[0]]
    for i in l1:
        if i!=result[-1]:
            result.append(i)

    return result

l=[1,2,2,3,4,5,5,6,2,2]

print(remove_duplicate_adjacents(l))