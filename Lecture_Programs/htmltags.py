import re

code="<h1>This is heading </h1>"

for m in re.finditer('^<h1>?</h1>$+',code):
    print(m.group(0))
    print("Index Position : " ,m.start())