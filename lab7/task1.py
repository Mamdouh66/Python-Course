# Write a comprehension over a range of the form range(n) such that the value
# of the comprehension is the set of odd numbers from 1 to 99.

if __name__ == "__main__":
    dct = {k: v for k, v in enumerate(range(1, 100)) if v % 2 != 0}
    print(dct)
