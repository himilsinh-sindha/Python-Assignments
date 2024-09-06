# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.

def count_strings(strings):
    count=0
    for s in strings:
        if len(s)>2 and s[0]==s[-1]:
            count+=1
    return count

l1=['aaaaa','babafb','cac','a','zabcz']

print(count_strings(l1))
