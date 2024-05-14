'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
from othello_board import OthelloBoard

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.depth = 5
    
    def get_move(self, board):
        return self.get_best_move(board)

    def minimax(self, board: OthelloBoard, depth, ismax):
        if depth == 0:
            return self.evaluate(board)
        
        legal_moves = board.get_legal_moves(self.symbol)

        if ismax:
            max_eval = float('-inf')
            for move in legal_moves:
                new_board = board.clone_of_board()
                new_board.play_move(move[0], move[1], self.symbol)
                eval = self.minimax(new_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                new_board = board.clone_of_board()
                new_board.play_move(move[0], move[1], self.symbol)
                eval = self.minimax(new_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def evaluate(self, board:OthelloBoard):
        return board.count_score(self.symbol) - board.count_score(self.oppSym)

    def get_best_move(self, board:OthelloBoard):
        best_move = None
        best_eval = float('-inf') if self.symbol == 'X' else float('inf')
        legal_moves = board.get_legal_moves(self.symbol)

        for move in legal_moves:
            new_board = board.clone_of_board()
            new_board.play_move(move[0], move[1], self.symbol)
            eval = self.minimax(new_board, self.depth - 1, False)
            if (self.symbol == 'X' and eval > best_eval) or (self.symbol == 'O' and eval < best_eval):
                best_eval = eval
                best_move = move
                print(best_move)
        return best_move
