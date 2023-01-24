camelCase = str(input("camelCase: "))
snake_case = ""
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case += "_"
        snake_case += camelCase[i].lower()
    else:
        snake_case += camelCase[i]
print("Snake case: " + snake_case)
