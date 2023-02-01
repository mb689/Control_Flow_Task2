import random

num = random.randint(1, 20)

count = 0

while count < 3:
    guess = int(input("Take a guess: "))
    if guess == num:
        print("Well done, you guess correctly")
        break
    elif guess < num:
        print("Incorrect, the number is bigger")
        count += 1
    elif guess > num:
        print("Incorrect, the number is smaller")
        count += 1

if count == 3:
    print(f"Unlucky, the number was {num}")