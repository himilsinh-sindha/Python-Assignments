# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple

def sort_by_last(tuples):
    tuples=sorted(tuples,key=lambda x:x[-1])
    return tuples

l1=[(1,2),(2,1),(3,5),(5,3),(7,4),(4,7)]

print(sort_by_last(l1))