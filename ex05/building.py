import sys
from string import punctuation


def main():
    """
    Count the number of characters, uppercase, lowercase,
    punctuation, space, digit, for a given input.
    input is either the program arguments, or is read from standard insput
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        exit(0)
    text: str = ""
    if len(sys.argv) < 2:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]

    spaces_chars = [' ', '\n', '\r']

    upper: int = 0
    lower: int = 0
    punctuation_count: int = 0
    digits: int = 0
    spaces: int = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in punctuation:
            punctuation_count += 1
        elif c in spaces_chars:
            spaces += 1
        elif c.isdigit():
            digits += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
