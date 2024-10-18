import pygame
import chess

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 512, 512  # Size of the chessboard window
SQUARE_SIZE = WIDTH // 8  # Each square is one-eighth of the board

# Load images for pieces
def load_images():
    images = {
        'r': 'black_rook.png',
        'n': 'black_knight.png',
        'b': 'black_bishop.png',
        'q': 'black_queen.png',
        'k': 'black_king.png',
        'p': 'black_pawn.png',
        'R': 'white_rook.png',
        'N': 'white_knight.png',
        'B': 'white_bishop.png',
        'Q': 'white_queen.png',
        'K': 'white_king.png',
        'P': 'white_pawn.png'
    }
    
    for piece, img_file in images.items():
        images[piece] = pygame.transform.scale(pygame.image.load(f'assets/{img_file}'), (SQUARE_SIZE, SQUARE_SIZE))
    
    return images

# Draw chessboard
def draw_board(screen):
    colors = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)]  # Light and dark square colors
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces on the board
def draw_pieces(screen, board, images):
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))  # Flip the board
            if piece:
                screen.blit(images[piece.symbol()], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Update the game window
def update_display(screen, board, images):
    draw_board(screen)
    draw_pieces(screen, board, images)
    pygame.display.flip()

# Main GUI loop
def chess_gui_loop(chess_game):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Voice-Controlled Chess')
    images = load_images()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_display(screen, chess_game.board, images)

    pygame.quit()