# write a program to check if the string only contains alphabets and digits:

import re

regObj0 = re.compile(r'^[a-zA-Z0-9]*$')
regObj1 = re.compile(r'^[a-z]+_[a-z]+$')
regObj2 = re.compile(r'ab*?')
regObj3 = re.compile(r'ab{3}?')


result = regObj.search("aabbb")

if result==None:
    print('Not Valid')
else:
    print('Valid')