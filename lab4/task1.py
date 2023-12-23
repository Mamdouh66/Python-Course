# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

if __name__ == "__main__":
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_nums = len([num for num in numbers if num % 2 == 0])
    odd_nums = len([num for num in numbers if num % 2 != 0])
    print(f"even nums ({even_nums}) & odd nums ({odd_nums})")
