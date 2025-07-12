due = 50
supported = [25, 10, 5]
while due > 0:
    print('Amount Due:', due)
    inserted = int(input('Insert Coin: '))
    if inserted in supported:
        due -= inserted
print('Change Owed:', abs(due))