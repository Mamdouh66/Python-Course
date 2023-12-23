# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


def yoda(s: str):
    return " ".join(s.split()[::-1])


if __name__ == "__main__":
    print(yoda("I am home"))
