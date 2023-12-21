if __name__ == "__main__":
    salary = int(input("Enter you salary >> "))

    if salary < 0:
        raise ValueError("Must be positive")

    print(salary * 12)
