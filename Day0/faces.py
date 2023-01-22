def main():
    string = str(input())
    print(convert(string))


def convert(string="You're welcome"):
    string = string.replace(":)", '🙂')
    string = string.replace(":(", '🙁')
    return string


main()
