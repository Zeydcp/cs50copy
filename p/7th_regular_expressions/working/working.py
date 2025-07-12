from re import search


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := search(r"^(\d{1,2}) (?:A|P)M to (\d{1,2}) (?:A|P)M$", s):
        if (
            int(match.group(1)) > 12
            or int(match.group(1)) == 0
            or int(match.group(2)) > 12
            or int(match.group(2)) == 0
        ):
            raise ValueError

        times = s.split(" to ")

        for count, time in enumerate(times):
            if pm := search(r"(\d{1,2}) PM", time):
                times[count] = f"{int(pm.group(1)) % 12 + 12}:00"

            elif am := search(r"(\d{1,2}) AM", time):
                times[count] = f"{int(am.group(1)) % 12:02}:00"

        return " to ".join(times)

    elif match := search(
        r"^(\d{1,2}):(\d{2}) (?:A|P)M to (\d{1,2}):(\d{2}) (?:A|P)M$", s
    ):
        if (
            int(match.group(1)) > 12
            or int(match.group(1)) == 0
            or int(match.group(3)) > 12
            or int(match.group(3)) == 0
            or int(match.group(2)) > 59
            or int(match.group(4)) > 59
        ):
            raise ValueError

        times = s.split(" to ")

        for count, time in enumerate(times):
            if pm := search(r"(\d{1,2}):(\d{2}) PM", time):
                times[count] = f"{int(pm.group(1)) % 12 + 12:02}:{int(pm.group(2)):02}"

            elif am := search(r"(\d{1,2}):(\d{2}) AM", time):
                times[count] = f"{int(am.group(1)) % 12:02}:{int(am.group(2)):02}"

        return " to ".join(times)

    else:
        raise ValueError


if __name__ == "__main__":
    main()