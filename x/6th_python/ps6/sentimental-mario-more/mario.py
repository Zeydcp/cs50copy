# TODO
from cs50 import get_int
while True:
    Height = get_int("Height: ")
    if Height > 0 and Height < 9:
         break

for i in range(1, Height + 1):
    for j in range(Height - i):
        print(" ", end="")

    for j in range(i):
        print("#", end="")

    print("  ", end="")

    for j in range(i):
        print("#", end="")

    print()
