def main():
    time = input('What time is it? ')

    if time.endswith('.'):
        time, meridian = time.split(' ')
        meridian = meridian[0]
        time = convert(time)
        if meridian == 'p':
            if time >= 12 or time <= 1:
                print('lunch time')
            elif 6 <= time <= 7:
                print('dinner time')
        elif 7 <= time <= 8:
            print('breakfast time')
    else:
        time = convert(time)
        if 7 <= time <= 8:
            print('breakfast time')
        elif 12 <= time <= 13:
            print('lunch time')
        elif 18 <= time <= 19:
            print('dinner time')


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    mins_in_hrs = float(minutes) / 60
    return hours + mins_in_hrs


if __name__ == "__main__":
    main()