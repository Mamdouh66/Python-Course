greet = str(input("Greeting: ")).strip().lower()

if greet.find("hello") == 0:
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")
