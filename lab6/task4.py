# Write a function that takes two positive integers that represent the numerator and denominator
# of a fraction as its only two parameters. The body of the function should reduce the fraction
# to lowest terms and then return both the numerator and denominator of the reduced fraction as
# its result. For example, if the parameters passed to the function are 6 and 63 then the function
# should return 2 and 21. Include a main program that allows the user to enter a numerator and denominator.
# Then your program should display the result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reduce_fraction(a: int, b: int):
    _gcd = gcd(a, b)
    return a // _gcd, b // _gcd


if __name__ == "__main__":
    print(reduce_fraction(6, 63))
