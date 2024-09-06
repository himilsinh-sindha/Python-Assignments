# Python program to get all subsets of a given size of a set

from itertools import combinations

def find_all_subsets(s, size):
    return list(combinations(s, size))

s = {1,2,3,4,5}
size = 2
print(find_all_subsets(s, size))
