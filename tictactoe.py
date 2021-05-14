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
