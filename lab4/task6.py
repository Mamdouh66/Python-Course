# Create a program that counts the number of elements within a list that are greater than 30.
# Here’s an example list you can use to test your work: num = [1,4,62,78,32,23,90,24,2,34].

if __name__ == "__main__":
    num = [1, 4, 62, 78, 32, 23, 90, 24, 2, 34]
    count = len([n for n in num if n > 30])
    print(count)
