if __name__ == "__main__":
    c = 10
    x, y, z = map(int, input("Enter values for x, y, z >>").split())
    q = (x * (c**3)) + (y + c**2) + (z * c)
    print(q)
