import math
import time
import random

#2: Define the TicTacToe class
class TicTacToe():
    # "def" = Keyword to define a function.   
    #"__init__" =  The name of the method. This is a special method name in Python, reserved for the constructor.  
    # "(self)" = The first parameter of the method. It refers to the instance of the class being created.
    def __init__(self): #This is the constructor method that initializes the TicTacToe object.
        self.board = self.make_board() #create an empty game board.
        self.current_winner = None #no winner at the start

    @staticmethod #his decorator indicates that make_board is a static method, meaning it doesn't depend on the instance (self) or class.
    def make_board():
        return [' ' for _ in range(9)] #Creates and returns a list of 9 empty spaces (' '), representing the 3x3 Tic-Tac-Toe board.

    #Prints the current state of the board in a readable format.
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]: #Splits the flat list self.board into 3 rows of 3 elements each.
            print('' + ' | '.join(row) + '') #Joins the elements of each row with ' | ' to create a visual represntation

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] #Creates a 3x3 grid of numbers from 0 to 8, representing the indices of the board.
        for row in number_board:
            print('' + ' | '.join(row) + '') #Joins the elements of each row with ' | ' to create a visual represntation
    
    # Attempts to place a player's letter (X or O) on the board at the specified square.
    def make_move(self, square, letter):
        if self.board[square] == ' ': #Checks if the square is empty.
            self.board[square] = letter #Places the player's letter on the board if the square is empty.
            if self.winner(square, letter): #Calls the winner method to check if this move results in a win.
                self.current_winner = letter #If the move results in a win, sets current_winner to the player's letter.
            return True #Returns True if the move was successful.
        return False #Returns False if the square was already occupied.

    #Checks if the current move results in a win for the player.
    def winner(self, square, letter): 
        # check the row
        row_ind = math.floor(square / 3) #Determines the row index of the square.
        row = self.board[row_ind*3:(row_ind+1)*3] #Extracts the row corresponding to the square.
        # print('row', row)
        if all([s == letter for s in row]): #Checks if all elements in the row match the player's letter.
            return True
        col_ind = square % 3 #Determines the column index of the square.
        column = [self.board[col_ind+i*3] for i in range(3)] #Extracts the column corresponding to the square.
        # print('col', column)
        if all([s == letter for s in column]):  Checks if all elements in the column match the player's letter.
            return True
        if square % 2 == 0: #hecks if the square is on a diagonal (only squares 0, 2, 4, 6, 8 are on diagonals).
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #Extracts the first diagonal (top-left to bottom-right).
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]): #Checks if all elements in either diagonal match the player's letter.
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]): #Checks if all elements in either diagonal match the player's letter.
                return True
        return False #Returns False if no winning condition is met.
        
    #Checks if there are any empty squares left on the board.
    def empty_squares(self):
        return ' ' in self.board #Returns True if there is at least one empty square (' '), otherwise False.

    #Counts the number of empty squares on the board.
    def num_empty_squares(self):
        return self.board.count(' ') #Returns the count of empty squares (' ') in the board.

    #Returns a list of indices of all empty squares.
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "] #Uses a list comprehension to find all indices (i) where the board value is ' '.


#3: Define the Player and its subclasses
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
            square = input(self.letter + '\'s turn. Input move (0-9): ')
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
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

#4: Define the play function
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
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

#5: Run the game
if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
