# Write a Python program to check the validity of password input by users.
# Validation :
# •	At least 1 letter between [a-z] and 1 letter between [A-Z].
# •	At least 1 number between [0-9].
# •	At least 1 character from [$#@].
# •	Minimum length 6 characters.
# •	Maximum length 16 characters.


if __name__ == "__main__":
    while True:
        try:
            password = input("Enter password >> ")
            small_char = 0
            upper_char = 0
            number = 0
            special_char = 0
            for i in password:
                if i.islower():
                    small_char += 1
                if i.isupper():
                    upper_char += 1
                if i.isdigit():
                    number += 1
                if i in ["$", "#", "@"]:
                    special_char += 1
            if small_char < 1:
                raise ValueError("At least 1 letter [a-z]")
            if upper_char < 1:
                raise ValueError("At least 1 letter [A-Z]")
            if number < 1:
                raise ValueError("At least 1 number [0-9]")
            if special_char < 1:
                raise ValueError("At least 1 special char [$#@]")
            if len(password) < 6 or len(password) > 18:
                raise ValueError("Must be 6 >= and <= 18")

            print("Password was saved..")
            break
        except ValueError as e:
            print(e)
