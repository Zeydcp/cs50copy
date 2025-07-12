from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(address):
    return f"Valid" if checkers.is_email(address) else f"Invalid"


if __name__ == "__main__":
    main()
