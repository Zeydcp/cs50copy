from inflect import engine

p = engine()
names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

my_list = p.join(names)
print()
print("Adieu, adieu, to", my_list)
