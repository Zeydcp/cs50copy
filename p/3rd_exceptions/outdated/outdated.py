months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ')
    is_letter = True if date[0].isalpha() else False
    try:
        if is_letter:
            month, day, year = date.split(' ')

            if ',' not in day:
                raise ValueError

            day, year = int(day.rstrip(',')), int(year)
            month = months.index(month) + 1
        else:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)

    except ValueError:
        pass
    
    else:
        if 0 < month < 13 and 0 < day < 32 and 0 < year < 2024:
            break

print(f"{year}-{month:02}-{day:02}")