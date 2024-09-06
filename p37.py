# check if a given string is binary or not

def check_binary(s):
    return set(s).issubset({'0', '1'})

str1 = "101010"
print(check_binary(str1))  

str2 = "101020"
print(check_binary(str2))
