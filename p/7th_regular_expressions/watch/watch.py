from re import search


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := search(
        r'<iframe .*src="(?:https?://)?(?:www\.)?youtube\.com/(?:embed/)?(\w+)".*></iframe>',
        s,
    ):
        return r"https://youtu.be/" + matches.group(1)


if __name__ == "__main__":
    main()
