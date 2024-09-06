import itertools

s={1,2,3,4,5,6,7,8,9,10}
n=int(input("Enter Length of Subset :"))
if(n > len(s)):
    print("Length is greater than the set size")
else:
    print(list(itertools.combinations(s,n)))
