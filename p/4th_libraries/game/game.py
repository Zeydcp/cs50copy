from random import randint

while True:
    try:
        n = int(input("Level: "))
        random = randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess not in range(1, n + 1):
            continue
        elif guess > random:
            print("Too large!")
            continue
        elif guess < random:
            print("Too small!")
            continue
        break

print("Just right!")
