# Check it two lists have at least one element in common

def have_common_element(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    return not set1.isdisjoint(set2)

l1 = [1, 2, 3]
l2 = [3, 4, 5]
print(have_common_element(l1, l2))
