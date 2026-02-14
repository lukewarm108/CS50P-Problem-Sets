import sys


def main():
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    code = sys.argv[1]
    try:
        with open(code, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                elif line.startswith("#"):
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(count)


if __name__ == "__main__":
    main()