import numpy as np

if __name__ == "__main__":
    array = np.array([1, -2, 3, -4, 5, -6, -7, 8, 9, -10])
    array[array < 0] = 0
    print(array)
