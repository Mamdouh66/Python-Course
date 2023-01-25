def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for i in range(len(s)):
                digitsInTheMiddle = []
                digitsInTheMiddle = s[1:-1]
                if digitsInTheMiddle.isnumeric() and s[-1].isalpha():
                    return False
                if s[i].isdigit() and s[i] != "0":
                    lastDigits = []
                    lastDigits = s[i:]
                    for j in range(len(lastDigits)):
                        if not lastDigits[j].isdigit():
                            return False
                    if not s.isalnum():
                        return False
                    else:
                        return True
                elif s[i] == "0":
                    return False
            if not s.isalnum():
                return False
            else:
                return True

    else:
        return False


main()
