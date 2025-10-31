import os

def clear_screen():
    """Clears the console screen for a clean display."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Step 1: Insert card
    print("Please insert your card...")
    input("[Press Enter]")
    clear_screen()

    # Step 2: Enter PIN
    pin = input("Enter your PIN: ..............")
    clear_screen()

    # Step 3: Choose account type
    while True:
        print("Choose your account type:")
        print("1. Savings")
        print("2. Current")
        print("3. Default")
        account_type = input("\nEnter your choice (1-3): ").strip()

        if account_type in ["1", "2", "3"]:
            clear_screen()
            break
        else:
            clear_screen()
            print("⚠️ Invalid choice! Please select 1, 2, or 3.\n")


    # Step 4: Show withdrawal options
    print("Choose withdrawal amount:")
    print("1. 1000 \t\t4. 10000")
    print("2. 2000 \t\t5. Other amount")
    print("3. 5000 \t\t6. Exit")
    amount_choice = input("\nEnter your choice (1-6): ")
    clear_screen()

    # Step 5: Setup account and values
    balance = 8000.0  # Starting balance
    withdrawal_amount = 0.0

    # Step 6: Handle user choice
    if amount_choice == "1":
        withdrawal_amount = 1000
    elif amount_choice == "2":
        withdrawal_amount = 2000
    elif amount_choice == "3":
        withdrawal_amount = 5000
    elif amount_choice == "4":
        withdrawal_amount = 10000
    elif amount_choice == "5":
        while True:
            try:
                withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
                break  # ✅ Exit loop if conversion successful
            except ValueError:
                print("\n⚠️ Invalid amount entered. Please enter a valid number.\n")

    elif amount_choice == "6":
        print("Transaction cancelled. Please collect your card.")
        return
    else:
        print("Invalid choice. Transaction cancelled.")
        return

    clear_screen()

    # Step 7: Check balance
    if withdrawal_amount > balance:
        print("Insufficient balance!")
        print(f"Your current balance is {balance}.")
        print("Please collect your card.")
        return

    # Deduct the amount
    balance -= withdrawal_amount

    # Screen 1: Transaction successful
    clear_screen()
    print("Transaction successful!")
    input("[Press Enter]")
    clear_screen()

    # Screen 2: Collect card
    print("Please collect your card.")
    input("[Press Enter]")
    clear_screen()

    # Screen 3: Collect money
    print(f"Please collect {withdrawal_amount}.")
    input("[Press Enter]")
    clear_screen()

    # Screen 4: Remaining balance
    print(f"Remaining balance: {balance}")
    input("[Press Enter]")
    clear_screen()

    # Final Screen
    print("Thank you for using our ATM!")
    input("[Press Enter to finish]")

# Run the program
if __name__ == "__main__":
    main()
