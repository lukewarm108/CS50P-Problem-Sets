import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n >= 1:
        break
    else: continue

answer = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess <= 0:
        continue
    elif guess > answer:
        print("Too large!")
        continue
    elif guess < answer:
        print ("Too small!")
        continue
    else:
        print("Just right!")
        break