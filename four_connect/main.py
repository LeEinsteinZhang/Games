import pygame
from pygame.locals import *
from logic import *
from display import *


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
                    show_message(screen, "The game ended with a draw.")
                else:
                    show_message(screen, f"Player {game.connect_has_won()} wins!")
                game = Connect()

    draw_board(screen, game, Connect)
    draw_current_player(screen, game.current_player)
    pygame.display.flip()

pygame.quit()
