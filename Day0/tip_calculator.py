def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d[1:]
    return float(d)


def percent_to_float(p):
    # TODO
    newP = float(p[:-1])
    return newP/100


main()
