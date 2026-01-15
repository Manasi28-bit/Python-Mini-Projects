import random

words = ["Guess", "Higher", "Close", "Jeans", "Timer", "Stopwatch", "Watch", "Suitcase", "Mango"]
word = random.choice(words).upper()

jumbled = list(word)
random.shuffle(jumbled)
jumbled_word = "".join(jumbled)

max_attempts = 3
attempts = 0

print("🔤 WORD JUMBLE GAME 🔤")

while attempts < max_attempts:
    print(f"\nJumbled word: {jumbled_word}")
    guess = input("Guess the word: ").strip().upper()

    if not guess:
        print("❌ Please enter a word.")
        continue

    attempts += 1

    if guess == word:
        print(f"\n🎉 You guessed it right in {attempts} attempts!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong guess! {remaining} attempt(s) left.")
        else:
            print(f"\n💥 GAME OVER! The correct word was: {word}")
