import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.fullmatch(pattern, s.strip())
    if not match:
        raise ValueError

    a = int(match.group(1))
    if match.group(2):
        b = int(match.group(2))
    else:
        b = 0
    m1 = match.group(3)

    c = int(match.group(4))
    if match.group(5):
        d = int(match.group(5))
    else:
        d = 0
    m2 = match.group(6)

    time1 = time_convert(a, b, m1)
    time2 = time_convert(c, d, m2)
    return f"{time1} to {time2}"    


def time_convert(x, y, z):
    x = int(x)
    y = int(y)
    if z == "AM":
        if x == 12:
            x = 00
    if z == "PM":
        if x != 12:
            x += 12
    return f"{x:02}:{y:02}"


if __name__ == "__main__":
    main()