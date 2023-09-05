import pygame
import sys
from const import *
from logic import *

pygame.init()
FONT = pygame.font.SysFont('Arial', 30)


def draw_board(screen, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                screen.blit(TETROMINO_SURFACES[cell], (j * BLOCK_SIZE, i * BLOCK_SIZE))


def draw_piece(screen, piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                screen.blit(piece.color, (piece.position[1] * BLOCK_SIZE + j * BLOCK_SIZE, piece.position[0] * BLOCK_SIZE + i * BLOCK_SIZE))


def draw_info(screen, score, speed):
    score_label = FONT.render(f'Score: {score}', True, (255, 255, 255))
    speed_label = FONT.render(f'Speed: {speed}', True, (255, 255, 255))
    screen.blit(score_label, (10, 10))
    screen.blit(speed_label, (10, 40))


def game_loop(screen):
    clock = pygame.time.Clock()
    grid = new_board()
    current_piece = Tetromino()
    game_over = False
    fall_time = 0
    score = 0
    speed_index = 1  # 默认中速

    while not game_over:
        screen.fill((0, 0, 0))
        fall_speed = SPEEDS[speed_index]
        fall_time += clock.get_rawtime()
        if fall_time > fall_speed:
            if not check_collision(grid, current_piece.shape, [current_piece.position[0] + 1, current_piece.position[1]]):
                current_piece.move_down()
            else:
                grid = join_matrix(grid, current_piece.shape, current_piece.template['id'], current_piece.position)
                cleared_lines, grid = clear_lines(grid)
                score += cleared_lines * (speed_index + 1) * 100  # 每清除一行得100分
                current_piece = Tetromino()
                if check_collision(grid, current_piece.shape, current_piece.position):
                    game_over = True
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(grid, current_piece.shape, [current_piece.position[0], current_piece.position[1] - 1]):
                    current_piece.move_left()
                elif event.key == pygame.K_RIGHT and not check_collision(grid, current_piece.shape, [current_piece.position[0], current_piece.position[1] + 1]):
                    current_piece.move_right()
                elif event.key == pygame.K_DOWN and not check_collision(grid, current_piece.shape, [current_piece.position[0] + 1, current_piece.position[1]]):
                    current_piece.move_down()
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if check_collision(grid, current_piece.shape, current_piece.position):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()
                elif event.key == pygame.K_1:
                    speed_index = 0  # 慢速
                elif event.key == pygame.K_2:
                    speed_index = 1  # 中速
                elif event.key == pygame.K_3:
                    speed_index = 2  # 快速

        draw_board(screen, grid)
        draw_piece(screen, current_piece)
        draw_info(screen, score, SPEED_LABELS[speed_index])
        pygame.display.flip()
        clock.tick(60)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    game_loop(screen)
main()
