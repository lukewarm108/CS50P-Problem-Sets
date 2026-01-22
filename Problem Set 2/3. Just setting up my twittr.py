def main():
    x = (input("Input: "))
    print(f"Output: {convert(x)}")

def convert(text):
    result = ""
    for y in text:
        if y.lower() not in "aeiou":
            result += y
    return result

main()