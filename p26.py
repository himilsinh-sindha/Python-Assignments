# 16.Range and enumerate functions in python ( to iterate over a list)
l1=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(l1)):
    print(i,l1[i])

for i,j in enumerate(l1):
    print(i,j)