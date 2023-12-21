import math


def to_fahrenheit(cel: float) -> float:
    return 9.0 / (5.0 * cel) + 32


def to_miles(kil: float) -> float:
    return 0.6214 * kil


def to_seconds(hrs: float) -> float:
    return hrs * 360


def average_score(val1: float, val2: float, val3: float, val4: float) -> float:
    return (val1 + val2 + val3 + val4) / 4


def get_distance(xa: float, xb: float, ya: float, yb: float) -> float:
    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


if __name__ == "__main__":
    while True:
        print("1. convert cel to fah")
        print("2. convert kil to mile")
        print("3. convert hrs to sec")
        print("4. average score")
        print("5. calcaute distance")
        print("6. exit")
        choice = int(input("Your choice >> "))

        match (choice):
            case 1:
                cel = float(input("Enter cel >> "))
                print(to_fahrenheit(cel))
            case 2:
                kil = float(input("Enter kil >> "))
                print(to_miles(kil))
            case 3:
                hrs = float(input("Enter hrs >> "))
                print(to_seconds(hrs))
            case 4:
                val1, val2, val3, val4 = map(int, input("Enter values >> ").split())
                print(average_score(val1, val2, val3, val4))
            case 5:
                xa, xb, ya, yb = map(int, input("Enter values >> ").split())
                print(get_distance(xa, xb, ya, yb))
            case _:
                break
