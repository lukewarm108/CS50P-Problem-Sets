import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    pattern = r"<iframe[^>]*src=\"http(s)?://(www\.)?youtube\.com/embed/([\w-]+)\"[^>]*"
    if match := re.search(pattern, s):
        url = match.group(3)
        return f"https://youtu.be/{url}"
    else:
        return None


if __name__ == "__main__":
    main()