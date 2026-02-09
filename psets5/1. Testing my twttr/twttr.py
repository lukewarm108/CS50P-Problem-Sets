def main():
    x = input("Input: ")
    print(f"Output: {shorten(x)}")


def shorten(word):
    result = ""
    for i in word:
        if i.lower() not in "aeiou":
            result += i
    return result


if __name__ == "__main__":
    main()