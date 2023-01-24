due = 50
SUM = 0
while True:
    print("Amount Due:", due)
    coins = int(input("Insert Coin: "))
    if coins in (5, 10, 25) and due > 0:
        due -= coins
        SUM += coins
        if due <= 0:
            break
        else:
            print("Amount Due:", due)
print("Change Owed:", abs(50-SUM))
