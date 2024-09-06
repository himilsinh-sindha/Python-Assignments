# 6.	remove empty strings from the list of strings

l1=["apple","banana","","orange","","mango"]
l1=[i for i in l1 if i]

print(l1)