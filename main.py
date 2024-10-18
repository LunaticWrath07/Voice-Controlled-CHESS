from voice_recognition import recognize_speech
from move_parser import parse_move
from chess_game import ChessGame
import chess_gui
import threading

def main():
    game = ChessGame()
    
    # Start the GUI in a separate thread
    chess_gui_thread = threading.Thread(target=chess_gui.chess_gui_loop, args=(game,))
    chess_gui_thread.start()
    
    while not game.board.is_game_over():
        # Capture the voice command
        recognized_text = recognize_speech()
        
        if recognized_text:
            # Parse the recognized text into a move
            move_dict = parse_move(recognized_text)
            
            if move_dict:
                # Try to apply the move to the game
                if game.apply_move(move_dict):
                    print(f"Move applied: {recognized_text}")
                else:
                    # Invalid move feedback
                    print(f"Invalid move: {recognized_text}. Please try again.")
            else:
                # Parsing failed feedback
                print("Could not parse the move. Please speak clearly.")
        else:
            # Speech recognition failed feedback
            print("Could not understand your command. Please try again.")
    
    # End of game feedback
    print("Game Over!")
    print(game.board.result())  # Print the result of the game

if __name__ == "__main__":
    main()