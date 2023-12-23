# Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]


if __name__ == "__main__":
    lst = [1, 2, 3]
    flag = True
    st = "mamdouh"
    tup = (1, 2, 3)
    dct = {"this is": "boring"}

    print(
        f"lst ({type(lst)}), flag ({type(lst)}), st ({type(st)}), tup ({type(tup)}), dct ({type(dct)})"
    )
