def main():
    x = input("camelCase: ")
    x = snake_case(x)
    print("snake_case: " + x)

def snake_case(camel):
    result = ""
    for y in camel:
        if y.isupper():
            y = f"_{y.lower()}"
            result += y
        else:
            result += y
    return result

main()