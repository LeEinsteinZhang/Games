from const import *
from block import *


def check_collision(grid, shape, offset):
    off_x, off_y = offset
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if i + off_x > len(grid) - 1 or j + off_y > len(grid[i]) - 1 or j + off_y < 0 or grid[i + off_x][j + off_y]:
                    return True
    return False

def remove_line(grid, line):
    del grid[line]
    return [[0 for _ in range(GRID_WIDTH)]] + grid

def join_matrix(grid, shape, shape_id, offset):
    off_x, off_y = offset
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                grid[i + off_x][j + off_y] = shape_id  # 使用 shape_id 而不是 color
    return grid

def new_board():
    board = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]
    return board

def clear_lines(grid):
    lines_to_clear = [i for i, row in enumerate(grid) if all(row)]
    for i in lines_to_clear:
        grid = remove_line(grid, i)
    return len(lines_to_clear), grid
