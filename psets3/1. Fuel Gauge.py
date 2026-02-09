def main():
    while True:
        try: 
            x, y = input("Fraction(X/Y): ").split("/")
            x = int(x)
            y = int(y)
            fuel = round(convert(x, y))
            if x > y or y == 0 or x < 0:
                raise ValueError
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def convert(a, b):
    f = (a / b) * 100
    return f

main()