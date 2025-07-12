def main():
    while True:
        fraction = input('Fraction: ')
        percentage = convert(fraction)
        if 0 <= percentage <= 100:
            break

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    decimal = round(x / y * 100)
    if x > y:
        raise ValueError
    return decimal


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()