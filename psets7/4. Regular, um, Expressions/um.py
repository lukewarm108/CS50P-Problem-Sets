import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    number = 0
    pattern = r"\bum\b"
    match = re.findall(pattern, s.strip().lower())
    return len(match)


if __name__ == "__main__":
    main()