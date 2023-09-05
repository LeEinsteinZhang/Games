import pygame
import sys
from block import TETROMINOS
from const import *
from logic import *


GREY_BORDER = pygame.transform.scale(pygame.image.load('../src/img/grey.png'), (BLOCK_SIZE, BLOCK_SIZE))
TETROMINO_SURFACES = {tetromino['id']: tetromino['color'] for tetromino in TETROMINOS}


class Button:
    def __init__(self, x, y, width, height, text, font, text_color, bg_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.text_color)
        screen.blit(text_surface, (self.x + (self.width - text_surface.get_width()) // 2, self.y + (self.height - text_surface.get_height()) // 2))

    def is_over(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height


def select_speed(screen, font):
    slow_button = Button(100, 150, 100, 50, "Slow", font, WHITE, BLUE)
    medium_button = Button(100, 220, 100, 50, "Medium", font, WHITE, BLUE)
    fast_button = Button(100, 290, 100, 50, "Fast", font, WHITE, BLUE)

    running = True
    while running:
        screen.fill(BLACK)
        slow_button.draw(screen)
        medium_button.draw(screen)
        fast_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if slow_button.is_over(pos):
                    return 0
                elif medium_button.is_over(pos):
                    return 1
                elif fast_button.is_over(pos):
                    return 2
        
        pygame.display.flip()

def game_over_screen(screen, font, score):
    screen.fill(BLACK)
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 100))
    
    new_game_button = Button(SCREEN_WIDTH // 2 - 100, 200, 200, 50, 'New Game', font, WHITE, BLUE)
    quit_button = Button(SCREEN_WIDTH // 2 - 100, 270, 200, 50, 'Quit', font, WHITE, BLUE)
    
    new_game_button.draw(screen)
    quit_button.draw(screen)
    
    return new_game_button, quit_button


def draw_board(screen, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                screen.blit(TETROMINO_SURFACES[cell], (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + BLOCK_SIZE + 50))

def draw_piece(screen, piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                screen.blit(piece.color, (piece.position[1] * BLOCK_SIZE + j * BLOCK_SIZE + BLOCK_SIZE, piece.position[0] * BLOCK_SIZE + i * BLOCK_SIZE + BLOCK_SIZE + 50))


def draw_info(screen, font, score, speed):
    score_label = font.render(f'Score: {score}', True, (255, 255, 255))
    speed_label = font.render(f'Speed: {speed}', True, (255, 255, 255))
    screen.blit(score_label, (10, 15))
    screen.blit(speed_label, (SCREEN_WIDTH / 2, 15))


def draw_border(screen):
    offset_y = 50  # 下移偏移量
    for i in range(GRID_HEIGHT + 2):
        screen.blit(GREY_BORDER, ((GRID_WIDTH + 1) * BLOCK_SIZE, i * BLOCK_SIZE + offset_y))  # Right border
        screen.blit(GREY_BORDER, (0, i * BLOCK_SIZE + offset_y))  # Left border

    for i in range(GRID_WIDTH + 2):
        screen.blit(GREY_BORDER, (i * BLOCK_SIZE, 0 + offset_y))  # Top border
        screen.blit(GREY_BORDER, (i * BLOCK_SIZE, (GRID_HEIGHT + 1) * BLOCK_SIZE + offset_y))  # Bottom border


def game_loop(screen, font, speed_index):
    clock = pygame.time.Clock()
    grid = new_board()
    current_piece = Tetromino()
    # paused = False
    game_over = False
    fall_time = 0
    score = 0

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
                score += cleared_lines * (speed_index + 1) * 100
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

        draw_board(screen, grid)
        draw_piece(screen, current_piece)
        draw_info(screen, font, score, SPEED_LABELS[speed_index])
        draw_border(screen)
        pygame.display.flip()
        clock.tick(60)
