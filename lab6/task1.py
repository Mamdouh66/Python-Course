# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar,
# or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing
# with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.


def palidrom(s: str):
    return s[::-1] == s


if __name__ == "__main__":
    print(palidrom("madam"))
