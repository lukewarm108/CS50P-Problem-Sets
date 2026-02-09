def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    elif not s.isalnum():
        return False
    seen_digit = False
    for y in s:
        if y.isdigit():
            if not seen_digit:
                if y == "0":
                    return False
                seen_digit = True
        else:
            if seen_digit:
                return False
    return True

main()