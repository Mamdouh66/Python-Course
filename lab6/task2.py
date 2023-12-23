def panigram(s: str):
    return len(set(s.replace(" ", "").lower())) == 26


if __name__ == "__main__":
    print(panigram("The quick brown fox jumps over the lazy dog"))
