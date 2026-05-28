import sys
from ft_filter import ft_filter


def main():
    """
    Take the first argument as a string and the second as a number
    return a list of separated word contained in the string
    that have a length greater than number
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        exit(0)

    try:
        n: int = int(sys.argv[2])
    except (ValueError):
        print("AssertionError: the arguments are bad")
        exit(0)
    s: str = sys.argv[1]

    words: list[str] = s.split()
    f = ft_filter(lambda word: len(word) > n, words)
    words = [word for word in f]

    print(words)


if __name__ == "__main__":
    main()
