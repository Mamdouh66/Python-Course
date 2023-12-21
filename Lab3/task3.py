import math


def circle_area(radius: float) -> float:
    return math.pi * radius**2


def square_area(s: float) -> float:
    return s**2


def sphere_area(radius: float) -> float:
    return 4 * math.pi * radius**2


if __name__ == "__main__":
    while True:
        print("1. Get circle area")
        print("2. Get square area")
        print("3. Get sphere area")
        print("4. Exit")
        choice = int(input("Your Choice >> "))

        match (choice):
            case 1:
                radius = float(input("enter values >> "))
                print(circle_area(radius))
            case 2:
                s = float(input("Enter values >> "))
                print(square_area(s))
            case 3:
                radius = float(input("enter values >> "))
                print(sphere_area(radius))
            case _:
                break
