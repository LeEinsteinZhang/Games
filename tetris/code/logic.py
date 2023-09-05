from const import *
from block import *


def check_collision(grid, shape, offset):
    x_shift, y_shift = offset
    for i in range(len(shape)):
        row = shape[i]
        for j in range(len(row)):
            cell = row[j]
            if cell:
                if (i + x_shift > len(grid) - 1) or \
                   (j + y_shift > len(grid[i]) - 1) or \
                   (j + y_shift < 0) or \
                   (grid[i + x_shift][j + y_shift]):
                    return True
    return False


def remove_line(grid, line):
    del grid[line]
    new_line = [[0] * GRID_WIDTH]
    return new_line + grid


def join_matrix(grid, shape, shape_id, offset):
    x_shift, y_shift = offset
    for i in range(len(shape)):
        row = shape[i]
        for j in range(len(row)):
            cell = row[j]
            if cell:
                grid[i + x_shift][j + y_shift] = shape_id
    return grid


def new_board():
    board = []
    for i in range(GRID_HEIGHT):
        row = []
        for j in range(GRID_WIDTH):
            row.append(0)
        board.append(row)
    return board


def clear_lines(grid):
    lines_to_clear = []
    for i, row in enumerate(grid):
        if all(row):
            lines_to_clear.append(i)
    lines_removed_count = 0
    for i in lines_to_clear:
        grid = remove_line(grid, i - lines_removed_count)
        lines_removed_count += 1

    return lines_removed_count, grid
