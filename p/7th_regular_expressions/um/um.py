from re import findall, IGNORECASE


def main():
    print(count(input("Text: ")))


def count(s):
    try:
        list_of_um = findall(r"\bum\b", s, IGNORECASE)
    except TypeError:
        return 0
    return len(list_of_um)


if __name__ == "__main__":
    main()