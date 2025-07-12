from sys import exit, argv
from csv import DictReader
from tabulate import tabulate

argl = len(argv)
if argl < 2:
    exit("Too few command-line arguments")
elif argl > 2:
    exit("Too many command-line arguments")
elif not argv[1].endswith(".csv"):
    exit("Not a CSV file")

try:
    with open(argv[1]) as file:
        reader = DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    exit("File does not exist")
