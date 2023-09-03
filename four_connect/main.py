import pygame
from pygame.locals import *
from logic import *


# CONSTANT
WHITE = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (50, 50, 50)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
CELL_SIZE = 100

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Connect 4')


def draw_current_player(player):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Current Player: {"RED" if player == 1 else "YELLOW"}', True, WHITE)
    screen.blit(text, (20, 10))


def draw_board(board):
    for row in range(Connect.HEIGHT):
        for col in range(Connect.WIDTH):
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE + 5, row * CELL_SIZE + 5 + 50, CELL_SIZE - 10, CELL_SIZE - 10))
            pygame.draw.circle(screen, WHITE,
                               (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)
            char = board.get_char(col, row)
            if char == 1:
                pygame.draw.circle(screen, RED,
                                   (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)
            elif char == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (int(col * CELL_SIZE + CELL_SIZE / 2), int(row * CELL_SIZE + CELL_SIZE / 2 + 50)), 40)


def show_message(message):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))

    button_width = 200
    button_height = 60
    button_x = (SCREEN_WIDTH - button_width) / 2
    button_y = SCREEN_HEIGHT / 2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    button_font = pygame.font.SysFont(None, 36)
    button_text = button_font.render("Continue", True, BLACK)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    while True:
        screen.fill(BLACK)
        screen.blit(text, text_rect.topleft)

        pygame.draw.rect(screen, WHITE, button_rect)
        screen.blit(button_text, button_text_rect.topleft)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return


game = Connect()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            col = event.pos[0] // CELL_SIZE
            game.connect_drop_piece(col)
            if game.connect_has_finished():
                if game.connect_has_won() == 0:
                    show_message("The game ended with a draw.")
                else:
                    show_message(f"Player {game.connect_has_won()} wins!")
                game = Connect()

    draw_board(game)
    draw_current_player(game.current_player)
    pygame.display.flip()

pygame.quit()

