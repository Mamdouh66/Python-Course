x, y, z = str(input()).split()

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    print(float(x) / float(z))
