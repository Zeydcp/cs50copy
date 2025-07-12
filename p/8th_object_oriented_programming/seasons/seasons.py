from datetime import date
from re import search
from sys import exit
from inflect import engine


def main():
    minutes = minutes_alive(input("Date of Birth: "))
    print(in_words(minutes))


def minutes_alive(dob):
    matches = search(r"^(\d{4})-(\d{2})-(\d{2})$", dob)
    if not matches:
        exit("Invalid date")

    difference = str(
        date.today()
        - date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
    )
    days = int(difference.split(" ", 1)[0])
    minutes = days * 1440

    return minutes


def in_words(mins):
    convert = engine()
    return convert.number_to_words(mins, andword="").capitalize() + f" minutes"


if __name__ == "__main__":
    main()
