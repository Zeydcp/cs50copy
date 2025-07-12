while True:
    fraction = input('Fraction: ')
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        decimal = x / y
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if decimal <= 1:
            break

if decimal >= 0.99:
    print('F')
elif decimal <= 0.01:
    print('E')
else:
    print(format(decimal, ".0%"))