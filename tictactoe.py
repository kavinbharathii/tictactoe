import pygame
import time

pygame.font.init()

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# display and visual variables
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')


line_x = width // 3
line_y = height // 3
line_color = (0,200,150)
x_color = (250, 200, 150)
o_color = (150, 250 ,200)

# function to draw x
def draw_x(pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.line(display, x_color, ((x * line_x) + (line_x // 4), (y * line_y) + (line_y // 4)), ((x * line_x) +  (3 * (line_x // 4)), (y * line_y) + (3 * (line_y // 4))), 2)
    pygame.draw.line(display, x_color, ((x * line_x) + (3 * (line_x // 4)), (y * line_y) + (line_y // 4)) , ((x * line_x) + (line_x // 4), (y * line_y) + (3 * (line_y // 4))), 2)

# function to draw o
def draw_o(pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.circle(display, o_color, (((x * line_x) +  (line_x // 2)), ((y * line_y) + (line_y // 2))), (3 * (line_x // 8)), 2)

# list that kepps track of what positoions have been used
available_pos = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] 

def available(pos):
    if pos in available_pos:
        return True

# gets the row, col data by the mouse click event
def get_mouse_pos():
    return (pygame.mouse.get_pos()[0] // line_x, pygame.mouse.get_pos()[1] // line_x)
    
# main loop of the program
def main():
    run = True
    turn = 0
    click = 0
    winner = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click += 1
                pos = get_mouse_pos()
                i = pos[0]
                j = pos[1]

                if available(pos):
                    if turn % 2 == 0:
                        draw_x(pos)
                        board[i][j] = 'x'
                    else:
                        draw_o(pos)
                        board[i][j] = 'o'
                
                try:
                    available_pos.remove(pos)
                    turn += 1
                except:
                    print('Slot already occupied')

                if click == 12:
                    run = False

        # draws the layout of the board
        if width % 3 == 0:
            if height % 3 == 0:
                pygame.draw.line(display, line_color, (0, line_y), (width, line_y), 2 )
                pygame.draw.line(display, line_color, (0, line_y * 2), (width, line_y * 2), 2 )
                pygame.draw.line(display, line_color, (line_x, 0), (line_x, height), 2 )
                pygame.draw.line(display, line_color, (line_x * 2, 0), (line_x * 2, height), 2 )
                pygame.display.flip()


# checks for a winner
        if len(available_pos) == 0:
            
            for i in range(len(board)):
                if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                    winner = board[i][0]
                    time.sleep(2)
                    run = False
                    
            for j in range(len(board[0])):
                if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
                    winner = board[0][j]

            if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                winner = board[0][0]
                    
            elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                winner = board[0][2]

            if winner != None:
                print(str(winner) + " " + 'Wins')
                time.sleep(2)
                run = False

            else:
                print('Tie')
                time.sleep(2)
                run = False

main()
