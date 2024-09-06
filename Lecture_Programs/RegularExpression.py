import re

#convert the word in the sentence
street = '21 Ramkrishana Road'
print(re.sub('Road$','Rd.',street))


#find all words starting with 'a' and 'e':
text='The following example creates an ArrayLIst with a capacity 500 and required is only 300'
l=re.findall(r'\s[Aae]\w+',text)
print(l)

#get the index of the digit in the sentence
for m in re.finditer('\d+',text):
    print(m.group(0))
    print("Index Position : " ,m.start())