import random

# Word lists by difficulty
easy_words = ["apple", "train", "tiger", "money", "banana"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephants", "diamond", "umbrella", "computer", "mountain"]

def choose_level():
    """Ask the user to choose difficulty and return a secret word."""
    print("---- Welcome to the Correct Word Guessing Game! ----")
    print("Choose a level: easy / medium / hard")
    
    level = input("Enter level: ").lower()
    if level == 'easy':
        return random.choice(easy_words)
    elif level == 'medium':
        return random.choice(medium_words)
    elif level == 'hard':
        return random.choice(hard_words)
    else:
        print("Invalid choice. Defaulting to EASY level.")
        return random.choice(easy_words)

def give_hint(secret, guess):
    """Return a hint showing correct letters in correct positions."""
    hint = ''
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += '_'
    return hint

def play_game():
    secret = choose_level()
    attempts = 0
    previous_guesses = []

    print("\nLet's begin! Try to guess the secret word.\n")

    while True:
        guess = input("Enter your guess: ").lower().strip()
        attempts += 1

        # Input validation
        if not guess.isalpha():
            print("Please enter only letters.")
            continue

        previous_guesses.append(guess)

        if guess == secret:
            print(f"Congratulations! You guessed the word '{secret}' in {attempts} attempts!")
            break
        else:
            hint = give_hint(secret, guess)
            print(f"Hint: {hint}")
            print(f"Previous guesses: {', '.join(previous_guesses)}\n")

    print("Game Over! Thanks for playing.\n")

def main():
    while True:
        play_game()
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye! See you next time.")
            break

# Run the game
main()
