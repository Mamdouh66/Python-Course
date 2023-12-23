# SUMMER OF '69: Return the sum of the numbers in the array, except ignore
# sections of numbers starting with a 6 and extending to the next 9 (every 6 will
# be followed by at least one 9). Return 0 for no numbers.


def summer_of_69(lst: list):
    total, flag = 0, False
    for i in lst:
        if not flag:
            if i == 6:
                flag = True
            else:
                total += i
        elif i == 9:
            flag = False
    return total


if __name__ == "__main__":
    print(summer_of_69([4, 5, 6, 7, 8, 9]))
