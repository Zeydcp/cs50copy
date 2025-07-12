from re import search


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = r"\d{1,3}"
    regEx = r"^{0}\.{0}\.{0}\.{0}$".format(number)
    if search(regEx, ip):
        hash_list = ip.split(".")
        for hash in hash_list:
            if int(hash) > 255:
                return False

        return True

    return False


if __name__ == "__main__":
    main()
