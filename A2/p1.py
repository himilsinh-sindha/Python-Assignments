def convert(words):
    l1=words.split();

    for i in l1:
        print(f"Word : {i}")
        print(f"Uppercase: {i.upper()}")
        print(f"Lowercase: {i.lower()}")
        print(f"Length: {len(i)}\n")

words = "Himilsinh Sindha"

convert(words)