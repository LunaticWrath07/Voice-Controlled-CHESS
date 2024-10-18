import re

# Parse the spoken command into a chess move
def parse_move(text):
    # Regular expressions for common patterns like "move e2 to e4" or "knight to f3"
    move_pattern = r"([a-h][1-8])\s?to\s?([a-h][1-8])"
    piece_move_pattern = r"(pawn|rook|knight|bishop|queen|king)\s?to\s?([a-h][1-8])"
    
    move_match = re.search(move_pattern, text)
    piece_move_match = re.search(piece_move_pattern, text)

    if move_match:
        return {"from": move_match.group(1), "to": move_match.group(2)}
    elif piece_move_match:
        piece = piece_move_match.group(1).lower()
        destination = piece_move_match.group(2)
        return {"piece": piece, "to": destination}
    else:
        print("Unrecognized move format.")
        return None
