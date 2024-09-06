# 21.	Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.


def count(num):
    if num>=10:
        return 'Number of donuts: many'
    else:
        return f'Number of donuts: {num}'

print(count(6))
print(count(20))