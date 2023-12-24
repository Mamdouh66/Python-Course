# To practice, write a function that adds two matrices together using list comprehensions.
# The function should take in two 2D lists of the same dimensions. Try to implement this in one line!
# sample output: [[-2, 3], [3, 2]]


def add_matrices(mat1, mat2):
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))
    ]


if __name__ == "__main__":
    print(add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]]))
