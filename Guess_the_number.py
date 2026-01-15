import random
import time

num = random.randint(1, 100)
count = 0
start = time.time()

while True:
    try:
        guess = int(input("Guess the number [1-100]: "))

        if guess < 1 or guess > 100:
            print("❌ Invalid input! Enter number between 1 and 100.")
            continue

        count += 1

        if guess > num:
            print("Guess Lower!", end=" ")
            print("You are far away!" if guess - num > 10 else "You are very close!")
        elif guess < num:
            print("Guess Higher!", end=" ")
            print("You are far away!" if num - guess > 10 else "You are very close!")
        else:
            end = time.time()
            print(f"\n🎉 Congrats! You guessed it right in {count} attempts.")
            print(f"⏱ Time taken: {round(end - start, 2)} seconds")
            break

    except ValueError:
        print("❌ Please enter a valid number.")
