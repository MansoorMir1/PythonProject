import random

def user_guess_game():
    print("\n🎮 Choose Difficulty Level:")
    print("1. Easy   (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard   (1-100)")

    level = input("Enter choice (1/2/3): ").strip()

    if level == "1":
        high = 10
    elif level == "2":
        high = 50
    elif level == "3":
        high = 100
    else:
        print("⚠️ Invalid choice! Defaulting to Medium (1-50).")
        high = 50

    number = random.randint(1, high)
    attempts = 0  # ✅ added attempt counter

    print(f"\n🔢 I selected a number between 1 and {high}. Try to guess it!")

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("⚠️ Enter *numbers only*!")
            continue

        guess = int(guess)
        attempts += 1  # count attempts ✅

        if guess < 1 or guess > high:
            print(f"⚠️ Number must be between 1 and {high}. Try again.")
        elif guess < number:
            print("📉 Too low, try again!")
        elif guess > number:
            print("📈 Too high, try again!")
        else:
            print(f"\n✅ Correct! The number was {number}.")
            print(f"🎯 You guessed it in {attempts} attempts.\n")  # ✅ show attempts
            break


def computer_guess_game():
    print("\n🤖 Think of a number and **do not tell me**.")
    print("I (Computer) will try to guess it!")

    while True:
        max_input = input("Enter the maximum number I should guess (e.g., 100): ").strip()
        if max_input.isdigit() and int(max_input) > 1:
            high = int(max_input)
            break
        else:
            print("⚠️ Enter a valid number greater than 1.")

    low = 1
    attempts = 0  # ✅ track attempts
    feedback = ""

    while feedback != "c":
        attempts += 1
        guess = random.randint(low, high)

        print(f"\nIs your number {guess}?")
        feedback = input("Enter (H)igh, (L)ow, or (C)orrect: ").lower().strip()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("⚠️ Please enter only H, L, or C.")

    print(f"\n🎉 Yay! I guessed your number: {guess}")
    print(f"🤖 It took me {attempts} attempts.\n")  # ✅ show attempts


def main():
    while True:
        print("\n------- 🎯 GUESSING GAME MENU 🎯 -------")
        print("1. You guess the computer's number")
        print("2. Computer guesses your number")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            user_guess_game()
        elif choice == "2":
            computer_guess_game()
        elif choice == "3":
            print("👋 Goodbye! Thanks for playing!")
            break
        else:
            print("⚠️ Invalid choice! Try again.")


main()
