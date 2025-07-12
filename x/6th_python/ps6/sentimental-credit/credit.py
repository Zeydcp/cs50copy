# TODO
from cs50 import get_int

while True:
    card_input = get_int("Number: ")
    if card_input >= 0:
        break

length = map(int, str(card_input))
length = len(list(length))

temp = map(int, str(card_input))
temp = list(temp)
temp.reverse()

temp2 = temp[::2]
temp = temp[1::2]
temp = [i * 2 for i in temp]

i = -1

for digit in temp:
    i += 1
    if digit > 9:
        temp3 = map(int, str(digit))
        temp3 = sum(list(temp3))
        temp[i] = temp3

sum = sum(temp) + sum(temp2)
if sum % 10 != 0:
    print("INVALID")
    exit(1)

card_input = str(card_input)

match length:
    case 13:
        print("VISA") if card_input[0] == "4" else print("INVALID")
    case 15:
        print("AMEX") if card_input[:2] == "34" or card_input[:2] == "37" else print(
            "INVALID"
        )
    case 16:
        if card_input[0] == "4":
            print("VISA")
        elif card_input[:2] > "50" and card_input[:2] < "56":
            print("MASTERCARD")
        else:
            print("INVALID")
    case _:
        print("INVALID")
