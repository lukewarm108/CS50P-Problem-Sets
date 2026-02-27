from datetime import date
import sys
import inflect


p = inflect.engine()


def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    try:
        s = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    if s > today:
        sys.exit("Invalid date")
    delta = today - s
    result = p.number_to_words(delta.days * 24 * 60, andword="")
    return f"{result.capitalize()} minutes"


if __name__ == "__main__":
    main()