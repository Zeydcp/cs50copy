from sys import exit, argv
from csv import DictReader, DictWriter

argl = len(argv)
if argl < 3:
    exit("Too few command-line arguments")
elif argl > 3:
    exit("Too many command-line arguments")

try:
    with open(argv[1]) as file:
        reader = DictReader(file)

        with open(argv[2], "w") as new_file:
            writer = DictWriter(new_file, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    exit(f"Could not read {argv[1]}")

