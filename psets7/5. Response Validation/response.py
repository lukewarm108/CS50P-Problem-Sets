from validator_collection import validators


def main():
    s = input("What's your email address? ")
    try:
        validators.email(s)
        print("Valid")
    except:
        print("Invalid")


if __name__ == "__main__":
    main()