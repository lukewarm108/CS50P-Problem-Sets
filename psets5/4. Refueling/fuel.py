def main():
    while True:
        try:
            a = input("Fraction: ")
            a = convert(a)
            a = gauge(a)
        except (ZeroDivisionError, ValueError):
            continue
        else:
            break
    print(a)


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y or x < 0 or y < 1:
        raise ValueError
    result = (x / y) * 100
    return round(result)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        Z = percentage
        return f"{Z}%"


if __name__ == "__main__":
    main()