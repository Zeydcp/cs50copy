from sys import exit, argv

argl = len(argv)
if argl < 2:
    exit("Too few command-line arguments")
elif argl > 2:
    exit("Too many command-line arguments")
elif not argv[1].endswith(".py"):
    exit("Not a Python file")

try:
    with open(argv[1]) as file:
        count = 0
        for line in file:
            if not (line.isspace() or line.lstrip().startswith("#")):
                count += 1
except FileNotFoundError:
    exit("File does not exist")

print(count)
