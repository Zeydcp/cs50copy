def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    if not 1 < len(s) < 7 or not s.isalnum():
        return False
    elif not s[:2].isalpha():
        return False

    for count, c in enumerate(s):
        if c.isnumeric() and c == '0':
            return False
        elif s[count:].isnumeric():
            return True
    return True


if __name__ == "__main__":
    main()