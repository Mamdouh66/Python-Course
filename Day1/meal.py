def main():
    time = input("What time is it? ")
    decimalTime = convert(time)

    if decimalTime >= 7.0 and decimalTime <= 8.0:
        print("breakfast time")
    elif decimalTime >= 12.0 and decimalTime <= 13.0:
        print("lunch time")
    elif decimalTime >= 18.0 and decimalTime <= 19.0:
        print("dinner time")


def convert(time):
    x, y = time.split(":")
    hours = float(x)
    minutes = float(y) / 60
    return hours+minutes


if __name__ == "__main__":
    main()
