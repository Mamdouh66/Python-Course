text = str(input("Input: ")).strip()
twttr = ""
for i in range(len(text)):
    if text[i].lower() not in ("a", "e", "i", "o", "u"):
        twttr += text[i]
print("Output: " + twttr)
