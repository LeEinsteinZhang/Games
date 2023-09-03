import pygame
import sys
from pygame.locals import *

WID_HEIGHT = 950
WID_WIDTH = 600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WID_WIDTH, WID_HEIGHT))

Image = pygame.image.load("../pic/yellow.png")
Rect = Image.get_rect()
Rect.center = (WID_WIDTH / 2, WID_HEIGHT / 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(Image, Rect)
    pygame.display.update()