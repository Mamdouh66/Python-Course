# Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.


def has_33(lst: list):
    return "".join(map(str, lst)).find("33") != -1


if __name__ == "__main__":
    print(has_33(([1, 3, 3])))
