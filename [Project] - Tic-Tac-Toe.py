import math
import time
import random

# 2:Define the TicTacToe class
class TicTacToe():
    def __init__(self):  #This is the constructor method that initializes the TicTacToe object.
        self.board = self.make_board()  #create an empty game board.
        self.current_winner = None  #no winner at the start

    #Creates and returns a list of 9 empty spaces (' ')
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]  

    #Prints the current state of the board in a readable format.
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('' + ' | '.join(row) + '')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('' + ' | '.join(row) + '')

    
    #The winner() method checks rows, columns, and diagonals
    #'self' is the instance to access the class
    def make_move(self, square, letter):  
        if self.board[square] == ' ':     #Checks if the selected square is empty (contains a space ' ')
            self.board[square] = letter    #Places the player's letter in the chosen square
            if self.winner(square, letter): #Calls the winner() method to check if this move created a winning line
                self.current_winner = letter #If so, sets current_winner to the player's letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3) #Converts a linear position (0-8) to a row index (0-2); Example: square 5 → 5/3 = 1.66 → floor to 1 (second row)
        row = self.board[row_ind * 3:(row_ind + 1) * 3] #Gets the full row from the board list
        if all([s == letter for s in row]): #checks if all squares in ROW match current player's letter
            return True
        # check the column
        col_ind = square % 3 #Gets column number; Example: suquare 7 => 7/3 = 2, 2nd column
        column = [self.board[col_ind + i * 3] for i in range(3)] #Gets the full Column from the board list
        if all([s == letter for s in column]): #checks if all squares in COLUMN match current player's letter
            return True
        # check diagonals
        if square % 2 == 0:#Gets Diagonal squares
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self): #checks whether there are any remaining empty spaces on the game board
        return ' ' in self.board #The 'in' operator checks if there's at least one empty space (' ') in the board list
        #Returns True if any space is empty, Returns False if all spaces are filled with 'X' or 'O'
        
    def num_empty_squares(self): #This method returns the exact count of remaining empty squares (' ') on the game board
        return self.board.count(' ')
        '''.count(' '):
            A built-in Python list method. 
            Scans the list and counts how many times the space character ' ' appears.
            Returns an integer count'''

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "] #Return only empty square's 'Index"'

# 3: Define the Player and its subclasses
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
            square = input(self.letter + '\'s turn. Input move (0-8): ')  # Changed from 0-9 to 0-8
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
        #.count(' '):
        #A built-in Python list method. 
        #Scans the list and counts how many times the space character ' ' appears.
        #Returns an integer count'''

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            # undo move
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


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
