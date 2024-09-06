# 9.	replace list's item with new value if found
l1=[1,2,3,4,5,6,7,8]
for i in range(len(l1)):
    if l1[i]==2:
        l1[i]=20
print(l1)