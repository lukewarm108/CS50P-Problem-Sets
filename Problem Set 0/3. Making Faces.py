def main():
    x = input("Your input: ")
    print(convert(x))

def convert(x):
    x = x.replace(":)", "🙂").replace(":(", "🙁")
    return x

main()