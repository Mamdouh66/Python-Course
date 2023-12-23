# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(s: str):
    return "".join([let * 3 for let in s])


if __name__ == "__main__":
    print(paper_doll("hello"))
