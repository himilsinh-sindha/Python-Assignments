# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.

def merge_list(l1,l2):
    l3=[]
    i=j=0

    while(i<len(l1) and j<len(l2)):

        if l1[i]<=l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    
    l3.extend(l1[i:])
    l3.extend(l2[j:])

    return l3


l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

print(merge_list(l1,l2))