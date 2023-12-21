if __name__ == "__main__":
    x = ("pies", "cake", "bread", "scone", "cookies")
    x = list(x)
    x[-1] = "tart"
    x = tuple(x)
    print(x)