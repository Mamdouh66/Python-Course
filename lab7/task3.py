# Implement a function coords, which takes a function, a sequence, and an upper and lower bound on output of the function.
# coords then returns a list of x, y coordinate pairs (lists) such that:
# •	Each pair contains [x, fn(x)]
# •	The x coordinates are the elements in the sequence
# •	Only pairs whose y coordinate is within the upper and lower bounds are included
# sample output : [[-2, 4], [1, 1], [3, 9]]
# One other thing: your answer can only be one line long. You should make use of list comprehensions!


def coords(fn, seq, lower, upper):
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]


if __name__ == "__main__":
    seq = [-4, -2, 0, 1, 3]
    fn = lambda x: x**2
    print(coords(fn, seq, 1, 9))
