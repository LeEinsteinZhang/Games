import pygame
import random
from const import *


TETROMINOS = [
    {'id': 'I', 'shape': [[1, 1, 1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/cyan.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'J', 'shape': [[0, 0, 1], [1, 1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/blue.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'L', 'shape': [[1, 0, 0], [1, 1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/orange.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'O', 'shape': [[1, 1], [1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/yellow.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'S', 'shape': [[0, 1, 1], [1, 1, 0]], 'color': pygame.transform.scale(pygame.image.load('../src/img/green.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'T', 'shape': [[0, 1, 0], [1, 1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/purple.png'), (BLOCK_SIZE, BLOCK_SIZE))},
    {'id': 'Z', 'shape': [[1, 1, 0], [0, 1, 1]], 'color': pygame.transform.scale(pygame.image.load('../src/img/red.png'), (BLOCK_SIZE, BLOCK_SIZE))}
]

class Tetromino:
    def __init__(self):
        self.template = random.choice(TETROMINOS)
        self.shape = self.template['shape']
        self.color = self.template['color']
        self.position = [0, GRID_WIDTH // 2 - len(self.shape[0]) // 2]

    def rotate(self):
        self.shape = [list(row) for row in zip(*reversed(self.shape))]

    def move_left(self):
        self.position[1] -= 1

    def move_right(self):
        self.position[1] += 1

    def move_down(self):
        self.position[0] += 1
