def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    number_started = False
    for i in s:
        if i.isdigit():
            if not number_started:
                if i == "0":
                    return False
                number_started = True
        else:
            if number_started:
                return False
    return True
    

if __name__ == "__main__":
    main()