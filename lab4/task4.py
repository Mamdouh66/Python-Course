# Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2


if __name__ == "__main__":
    st = input("Enter >> ")
    sct = 0
    dct = 0
    for i in st:
        if i.isdigit():
            dct += 1
        elif i.isalpha():
            sct += 1

    print(f"number of letter ({sct}), number of digit ({dct})")
