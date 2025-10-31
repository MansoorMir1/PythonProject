# ##          Simple Calculator in python

# print(eval(input("enter you want : ")))        


###############################


import os

HISTORY_FILE = "history.txt"

# ----- Functions -----
def show_history():
    """Show saved calculations."""
    if not os.path.exists(HISTORY_FILE):
        print("📭 No history found!")
        return

    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()

    if not lines:
        print("📭 No history found!")
        return

    print("\n📜 --- Calculation History ---")
    for line in reversed(lines):
        print(line.strip())
    print("-------------------------------\n")


def clear_history():
    """Clear all saved calculations."""
    with open(HISTORY_FILE, "w") as file:
        pass
    print("🧹 History cleared!\n")


# def save_history(expression, result):
#     """Save a single calculation or logic result to history."""
#     with open(HISTORY_FILE, "a") as file:
#         file.write(f"{expression} = {result}\n")


def calculate(raw_expression):
    """
    Evaluate a math/logical expression safely.
    Supports +, -, *, /, //, %, **, (), [], and, or, not, <, >, <=, >=, ==, !=
    """
    # Allowed characters and words
    allowed_chars = "0123456789+-*/%.()[]<>=! "
    allowed_words = {"and", "or", "not", "True", "False"}

    expression = raw_expression.strip()

    # Validate characters
    for char in expression:
        if char not in allowed_chars and not char.isalpha():
            print(f"🚫 Invalid character detected: '{char}'")
            print("⚠️ Use only numbers, + - * / // % ** () [] and logical operators.")
            return

    # Validate words
    for word in expression.split():
        if word.isalpha() and word not in allowed_words:
            print(f"🚫 Invalid word detected: '{word}'")
            print("⚠️ Allowed logical words: and, or, not, True, False")
            return

    # Convert square brackets to parentheses
    expression_for_eval = expression.replace('[', '(').replace(']', ')')

    try:
        # Evaluate safely
        result = eval(expression_for_eval)

        # Convert whole floats to int
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print(f"✅ Result: {result}")
        # save_history(expression, result)

    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    except Exception:
        print("⚠️ Invalid expression! Please check your syntax.")
''' 
Code Part	                Purpose	                    Example Trigger      Message Shown
except ZeroDivisionError:	Catches division by zero	 10 / 0	❌          Error: Division by zero is not allowed.
except Exception:	        Catches all other errors	 5 + * 6, 7 + [8	⚠️ Invalid expression! Please check your syntax.  
'''

# ----- Main Program -----
def main():
    print("🧮 --- Advanced Math & Logic Calculator ---")
    print("Supports:")
    print("  ➕ Math: +  -  *  /  //  %  **  ( )  [ ]")
    print("  🧠 Logic: and  or  not  <  >  <=  >=  ==  !=")
    print("Type commands: history | clear | exit\n")

    while True:
        user_input = input("Enter expression or command: ").strip()

        if user_input.lower() == "exit":
            print("\n👋 Goodbye! Thanks for using the calculator.")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        elif user_input == "":
            continue
        else:
            calculate(user_input)


# Run program
if __name__ == "__main__":
    main()

