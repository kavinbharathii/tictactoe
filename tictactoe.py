import pygame
import time

pygame.font.init()

# display and visual variables
width = 600
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')


line_x = width // 3
line_y = height // 3
line_color = (0, 200, 150)
x_color = (250, 200, 150)
o_color = (150, 250, 200)


class Tacboard(object):
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    def draw_x(self, pos):
        x = pos[0]
        y = pos[1]
        if self.available((x, y)):
            pygame.draw.line(display, x_color, ((x * line_x) + (line_x // 4), (y * line_y) + (line_y // 4)),
                             ((x * line_x) + (3 * (line_x // 4)), (y * line_y) + (3 * (line_y // 4))), 2)
            pygame.draw.line(display, x_color, ((x * line_x) + (3 * (line_x // 4)), (y * line_y) +
                                                (line_y // 4)), ((x * line_x) + (line_x // 4), (y * line_y) + (3 * (line_y // 4))), 2)

            self.board[pos[0]][pos[1]] = 1

        else:
            print(f"Position [{x},{y}] already occupied")

    def draw_o(self, pos):
        x = pos[0]
        y = pos[1]
        if self.available((x, y)):
            pygame.draw.circle(display, o_color, (((x * line_x) + (line_x // 2)),
                                                  ((y * line_y) + (line_y // 2))), (3 * (line_x // 8)), 2)

            self.board[pos[0]][pos[1]] = -1

        else:
            print(f"Position [{x},{y}] already occupied")

    def available(self, pos):
        return self.board[pos[0]][pos[1]] == 0

    def state(self):

        # winning states for X or O
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[1][1] if self.board[1][1] != 0 else None

        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1] if self.board[1][1] != 0 else None

        else:
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                    return self.board[i][0] if self.board[i][0] != 0 else None

            for j in range(3):
                if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                    return self.board[0][j] if self.board[0][j] != 0 else None

        return None

    def draw_board(self):
        # draws the layout of the board
        if width % 3 == 0:
            if height % 3 == 0:
                pygame.draw.line(display, line_color,
                                 (0, line_y), (width, line_y), 2)
                pygame.draw.line(display, line_color,
                                 (0, line_y * 2), (width, line_y * 2), 2)
                pygame.draw.line(display, line_color,
                                 (line_x, 0), (line_x, height), 2)
                pygame.draw.line(display, line_color,
                                 (line_x * 2, 0), (line_x * 2, height), 2)
                pygame.display.flip()

    def full(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return False

        return True


def get_mouse_pos():
    return (pygame.mouse.get_pos()[0] // line_x, pygame.mouse.get_pos()[1] // line_x)
