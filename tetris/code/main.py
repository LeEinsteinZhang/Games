import pygame
from const import *
from display import *
from logic import *


pygame.init()
FONT = pygame.font.SysFont('Arial', 16)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    
    speed_index = select_speed(screen, FONT)
    game_loop(screen, FONT, speed_index)

main()
