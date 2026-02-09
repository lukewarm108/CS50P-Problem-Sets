import random

def main():
    n = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        for j in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if x + y == ans:
                score += 1
                break
            else:
                print("EEE")
                continue
        else:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()