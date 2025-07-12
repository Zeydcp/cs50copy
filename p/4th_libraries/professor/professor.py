from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for i in range(3):
            try:
                answer = int(input("{} + {} = ".format(x, y)))
            except ValueError:
                pass
            else:
                if answer == x + y:
                    score += 1
                    break

            print("EEE")
            if i == 2:
                print(x, "+", y, "=", x + y)

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                break

    return level


def generate_integer(level):
    if level == 1:
        integer = randint(0, 10)
    else:
        integer = randint(10 ** (level - 1), 10**level)
    return integer


if __name__ == "__main__":
    main()
