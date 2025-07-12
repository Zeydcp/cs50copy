from sys import exit, argv
from os.path import splitext
from PIL.Image import open
from PIL.ImageOps import fit

argl = len(argv)
valid_ext = [".jpeg", ".jpg", ".png"]
if argl < 3:
    exit("Too few command-line arguments")
elif argl > 3:
    exit("Too many command-line arguments")

actual_ext = [splitext(argv[1])[1].lower(), splitext(argv[2])[1].lower()]

if actual_ext[0] not in valid_ext:
    print(actual_ext[0])
    exit("Invalid input")
elif actual_ext[1] not in valid_ext:
    exit("Invalid output")
elif actual_ext[0] != actual_ext[1]:
    exit("Input and output have different extensions")

try:
    before = open(argv[1])
except FileNotFoundError:
    exit("Input does not exist")

try:
    shirt = open("shirt.png")
except FileNotFoundError:
    exit("shirt.png does not exist")

size = shirt.size
after = before.copy()
after = fit(after, size)
after.paste(shirt, shirt)
after.save(argv[2])

before.close()
shirt.close()
