''' 
Work flow of project:
1. input from user(Rock, Paper, Scissor)
2. computer choice(Computer choose randomly)
3. results print

Cases:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Scissor win

B- Paper
Paper - Paper = Tie
Paper - rock = Paper win
Paper - Scissor = Scissor win

B- Scissor
Scissor - Scissor = Tie
Scissor - rock = Scissor win
Scissor - Paper = Scissor win

'''
import random

item = ['r','p','s']

# Counters for statistics
total_games = 0
user_wins = 0
comp_wins = 0
ties = 0

while True:
    # Ask user for input
    user_choice = input("Enter Your move : R --> Rock, P --> Paper, S --> Scissor = ").lower()

    # Validate user input
    if user_choice not in item:
        print("❌ Invalid choice! Please enter R --> Rock, P --> Paper, S --> Scissor.")
        continue  # Ask again

    # Computer makes a random choice
    comp_choice = random.choice(item)

    print(f'User choice = {user_choice}, Computer choice = {comp_choice}')

    # Game logic (kept exactly as original)
    total_games += 1
    if user_choice == comp_choice:
        print("🤝 It's a tie!")
        ties += 1

    elif user_choice == 'r':
        if comp_choice == 's':
            print("🪨 Rock smashes Scissor — You win! 🏆")
            user_wins += 1
        else:
            print("📄 Paper covers Rock — Computer wins! 💀")
            comp_wins += 1

    elif user_choice == 'p':
        if comp_choice == 'r':
            print("📄 Paper covers Rock — You win! 🏆")
            user_wins += 1
        else:
            print("✂️ Scissor cuts Paper — Computer wins! 💀")
            comp_wins += 1

    elif user_choice == 's':
        if comp_choice == 'r':
            print("✂️ Scissor cuts Paper — You win! 🏆")
            user_wins += 1
        else:
            print("🪨 Rock smashes Scissor — Computer wins! 💀")
            comp_wins += 1

    # Ask user if they want to play again
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            break
        print("⚠️ Please enter only 'y' or 'n'.")

    if play_again == "n":
        print("\n📊 Game Summary:")
        print(f"Total games played: {total_games}")
        print(f"You won: {user_wins} times")
        print(f"Computer won: {comp_wins} times")
        print(f"Ties: {ties}")
        print("\n👋 Thanks for playing! See you next time.")
        break

     