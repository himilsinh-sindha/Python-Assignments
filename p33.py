# 22.	Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.

def combine(str1,str2):
    str3=str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
    return str3

print(combine('mix','pod')) # 'pox mid'
print(combine('dog','dinner')) # 'dig donner'