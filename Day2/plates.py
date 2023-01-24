def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in range(len(s)):
        if s[i] in (".", " ", ","):
            return False
        if s[i].isdigit():
            digits = s[i].rsplit()
            for i in range(len(digits)):
                if not int(digits[i]) >= 0 and int(digits[i]) <= 9:
                    return False
        if not s[0].islower() and s[1].islower():
            return False
    return True


main()
