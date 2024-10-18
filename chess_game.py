
import chess
import move_parser

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def apply_move(self, move_dict):
        # For example, move_dict could be {'piece': 'pawn', 'square': 'e4'}
        if move_dict is None:
            print("Invalid move format!")
            return False

        piece = move_dict.get('piece')
        square = move_dict.get('square')

        # Identify legal moves for the piece and apply the move
        for legal_move in self.board.legal_moves:
            if chess.square_name(legal_move.to_square) == square.lower():
                move = legal_move
                break
        else:
            print("Illegal move!")
            return False

        # Apply the move to the board
        self.board.push(move)  # Updates the board with the move
        print(f"Move applied: {move}")
        return True

    def display_board(self):
        print(self.board)
