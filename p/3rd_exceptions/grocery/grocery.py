groceries = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

groceries = dict(sorted(groceries.items()))
for i in groceries:
    print(groceries[i], i.upper())