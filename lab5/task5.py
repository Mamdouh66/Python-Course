import math

# Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters.
# Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result.
# Include a main program that reads the lengths of the shorter sides of a right triangle from the user,
# uses your function to compute the length of the hypotenuse and displays the result.

if __name__ == "__main__":
    hyp = lambda x, y: math.sqrt(x**2 + y**2)
    print(hyp(3, 4))
