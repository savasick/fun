import copy
import pygame as pg
from random import randint

# Constants
WIDTH_COUNT, HEIGHT_COUNT = 120, 75
SIZE = 10
RESOLUTION = WIDTH, HEIGHT = WIDTH_COUNT * SIZE + 1, HEIGHT_COUNT * SIZE + 1
FPS = 6000
GRID_COLOR = (78, 78, 78)
ALIVE_COLOR = (255, 255, 255)

# Initialize pygame
screen = pg.display.set_mode(RESOLUTION)
clock = pg.time.Clock()

# Initialize game state
next_blocks_stage = [[0 for _ in range(WIDTH_COUNT)] for _ in range(HEIGHT_COUNT)]
blocks = [[randint(0, 1) for _ in range(WIDTH_COUNT)] for _ in range(HEIGHT_COUNT)]

def count_neighbors(field, pos):
    x, y = pos
    neighbors = 0
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            if x_offset == 0 and y_offset == 0:
                continue
            x_neighbor, y_neighbor = x + x_offset, y + y_offset
            if 0 <= x_neighbor < WIDTH_COUNT and 0 <= y_neighbor < HEIGHT_COUNT:
                neighbors += field[y_neighbor][x_neighbor]
    return neighbors

def update_block(field, pos):
    x, y = pos
    neighbors = count_neighbors(field, pos)
    if field[y][x]:
        return 1 if neighbors in (2, 3) else 0
    else:
        return 1 if neighbors == 3 else 0

def draw_grid():
    for x in range(0, WIDTH, SIZE):
        pg.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, SIZE):
        pg.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

def draw_blocks(field):
    for y, row in enumerate(field):
        for x, block in enumerate(row):
            if block:
                pg.draw.rect(screen, ALIVE_COLOR, (x * SIZE + 2, y * SIZE + 2, SIZE - 2, SIZE - 2))

def reset_game():
    global blocks, next_blocks_stage
    blocks = [[randint(0, 1) for _ in range(WIDTH_COUNT)] for _ in range(HEIGHT_COUNT)]
    next_blocks_stage = [[0 for _ in range(WIDTH_COUNT)] for _ in range(HEIGHT_COUNT)]
    screen.fill(pg.Color('black'))  # Clear the screen
    draw_grid()  # Redraw the grid
    pg.display.flip()  # Update the display

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                reset_game()

    screen.fill(pg.Color('black'))
    draw_grid()

    for y, row in enumerate(blocks):
        for x, block in enumerate(row):
            next_blocks_stage[y][x] = update_block(blocks, (x, y))

    blocks = copy.deepcopy(next_blocks_stage)
    draw_blocks(blocks)

    pg.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pg.display.flip()