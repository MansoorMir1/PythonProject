import math
import random
import time

# ------------- PLAYER CLASSES ------------- #

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"\n{self.letter}'s turn. Enter move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("⚠️  Not a valid move. Try again.")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)['position']

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1)
                if other_player == max_player
                else -1 * (state.num_empty_squares() + 1)
            }

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


# ------------- GAME CLASS ------------- #

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    @staticmethod
    def print_board_nums():
        print("\nBoard Positions (Reference):")
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(s == letter for s in row):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all(s == letter for s in col):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            if all(s == letter for s in diag1):
                return True

            diag2 = [self.board[i] for i in [2,4,6]]
            if all(s == letter for s in diag2):
                return True

        return False


# ------------- GAME LOOP (UI IMPROVED) ------------- #
def play(game, x_player, o_player, print_game=True):

    if print_game:
        print("\n🎮 ---- Tic Tac Toe ----")
        TicTacToe.print_board_nums()
        print("\nGame Start!\n")

    letter = 'X'

    while game.empty_squares():

        square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(f"\n✅ {letter} placed at position {square}")
                game.print_board()
                print("-" * 5)

            if game.current_winner:
                print(f"\n🎉 {letter} WINS THE GAME! 🎉\n")
                return letter

            letter = 'O' if letter == 'X' else 'X'
            if print_game:
                time.sleep(.9)

    if print_game:
        print("\n🤝 It's a TIE!\n")
    return None



# ------------- MAIN GAME RUNNER ------------- #

if __name__ == '__main__':
    print("\n🎮 Choose Game Mode:\n")
    print("1. Human vs Human")
    print("2. Human vs Random Computer")
    print("3. Human vs Smart Computer (AI)")
    print("4. Random Computer vs Random Computer")
    print("5. Random Computer vs Human")
    print("6. Random Computer vs Smart Computer (AI)")
    print("7. Smart Computer (AI) vs Human")
    print("8. Smart Computer (AI) vs Random Computer")
    print("9. Smart Computer (AI) vs Smart Computer (AI)\n")

    # Keep asking until valid input
    while True:
        choice = input("Enter choice (1-9): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 9:
            choice = int(choice)
            break
        print("⚠️ Invalid choice! Please enter a number between 1 and 9.\n")
    # List of mode player setups
    modes = [
        (HumanPlayer('X'), HumanPlayer('O')),
        (HumanPlayer('X'), RandomComputerPlayer('O')),
        (HumanPlayer('X'), SmartComputerPlayer('O')),
        (RandomComputerPlayer('X'), RandomComputerPlayer('O')),
        (RandomComputerPlayer('X'), HumanPlayer('O')),
        (RandomComputerPlayer('X'), SmartComputerPlayer('O')),
        (SmartComputerPlayer('X'), HumanPlayer('O')),
        (SmartComputerPlayer('X'), RandomComputerPlayer('O')),
        (SmartComputerPlayer('X'), SmartComputerPlayer('O')),
    ]

    x_player, o_player = modes[choice - 1]

    # Scoreboard
    x_wins = 0
    o_wins = 0
    ties = 0
    rounds = 0

    print("\n⚔️ Starting Matches...\n")

    while True:
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=True)
        rounds += 1

        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

        again = input("\n🔁 Play again? (y/n): ").lower().strip()
        if again != 'y':
            break

    print("\n📊 ---- Final Results ----")
    print(f"Rounds Played : {rounds}")
    print(f"X Wins        : {x_wins}")
    print(f"O Wins        : {o_wins}")
    print(f"Ties          : {ties}")
    print("\n🎯 Thanks for playing!\n")

