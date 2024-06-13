import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the board
board = [['' for _ in range(3)] for _ in range(3)]

# Define player symbols
player = 'X'

def draw_board():
    screen.fill(white)
    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, black, (0, i * 100), (width, i * 100), 3)
        pygame.draw.line(screen, black, (i * 100, 0), (i * 100, height), 3)

    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, black, (col * 100 + 15, row * 100 + 15), ((col + 1) * 100 - 15, (row + 1) * 100 - 15), 3)
                pygame.draw.line(screen, black, ((col + 1) * 100 - 15, row * 100 + 15), (col * 100 + 15, (row + 1) * 100 - 15), 3)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, black, (col * 100 + 50, row * 100 + 50), 45, 3)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col

def check_win():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

def restart_game():
    global board, player
    board = [['' for _ in range(3)] for _ in range(3)]
    player = 'X'
    draw_board()
    pygame.display.update()

# Draw the initial empty board
draw_board()
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse((x, y))

            # Update the board if the cell is empty
            if board[row][col] == '':
                board[row][col] = player
                winner = check_win()
                if winner:
                    print(f"{winner} wins!")
                    pygame.time.wait(2000)
                    restart_game()
                elif check_draw():
                    print("It's a draw!")
                    pygame.time.wait(2000)
                    restart_game()
                else:
                    player = 'O' if player == 'X' else 'X'
                draw_board()
                pygame.display.update()
                
pygame.quit()
sys.exit()
