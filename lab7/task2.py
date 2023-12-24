# Using range, write a comprehension whose value is a dictionary. The keys should be the integers
# from 0 to 99 and the value corresponding to a key should be the square of the key.

if __name__ == "__main__":
    dct = {k: k**2 for k in range(100)}
    print(dct)
