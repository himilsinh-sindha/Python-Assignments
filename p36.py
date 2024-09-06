# Python program to count number of vowels using sets in given string

def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return sum(1 for char in s if char in vowels)

s = "Himilsinh"
print(count_vowels(s)) 
