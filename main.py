import math
import random
import pygame
import tkinter
from stills import *
from oscillators import *
from spaceships import *
from grid import Grid

# Init some colors
BLACK = (0, 0, 0)
GREY = (140, 140, 140)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (200, 255, 200)
YELLOW = (127, 127, 0)
RED = (255, 200, 200)

# Define world size
WORLD_SIZE = 60
# Seems reasonable
assert WORLD_SIZE >= 4
c_width = c_height = 10
# Makes things easier
assert c_width % 2 == 0
margin = 3
# Again, laziness
assert margin % 2 == 1
w_width = (c_width * WORLD_SIZE) + (margin * (WORLD_SIZE + 1))
w_height = (c_height * WORLD_SIZE) + (margin * (WORLD_SIZE + 1))
size = (w_width, w_height)
done = False


def generate_world_row(row_len=WORLD_SIZE):
    return [round(random.random()) for x in range(row_len)]


def get_next_state(cur_world):
    global WORLD_SIZE
    new_state = [[0] * WORLD_SIZE for x in range(WORLD_SIZE)]
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            neighbors = get_neighbors_set(i, j)
            live_neighbors = 0
            for n in neighbors:
                live_neighbors += cur_world[n[0]][n[1]]
            if not cur_world[i][j] and live_neighbors == 3:
                new_state[i][j] = 1
            elif cur_world[i][j] and 2 <= live_neighbors <= 3:
                new_state[i][j] = 1
            else:
                new_state[i][j] = 0
    return new_state


def get_neighbors_set(x, y):
    global WORLD_SIZE
    neighbors = []
    xs = [x - 1, x, x + 1]
    ys = [y - 1, y, y + 1]
    if x == 0:
        xs.pop(0)
        xs.append(WORLD_SIZE - 1)
    elif x == WORLD_SIZE - 1:
        xs.pop(-1)
        xs.append(0)
    if y == 0:
        ys.pop(0)
        ys.append(WORLD_SIZE - 1)
    elif y == WORLD_SIZE - 1:
        ys.pop(-1)
        ys.append(0)
    for xc in xs:
        for yc in ys:
            if not (xc == x and yc == y):
                neighbors.append((xc, yc))
    return neighbors


def init_pattern(pattern):
    if hasattr(pattern, 'PATTERN') and hasattr(pattern, 'GRID_SIZE'):
        init_grid = pattern.PATTERN
        return inflate_world(init_grid, pattern.GRID_SIZE)
    return None


def inflate_world(subworld, init_grid=None):
    init_x = len(subworld[0])
    init_y = len(subworld)
    x_diff = WORLD_SIZE - init_grid[0] if init_grid and type(init_grid) == tuple else WORLD_SIZE - init_x
    y_diff = WORLD_SIZE - init_grid[1] if init_grid and type(init_grid) == tuple else WORLD_SIZE - init_y
    for row in subworld:
        if x_diff and len(row) < WORLD_SIZE:
            row += [0] * x_diff
    if y_diff:
        while len(subworld) < WORLD_SIZE:
            subworld.append([0] * WORLD_SIZE)
    return subworld


def init_world(seed_size):
    seed_world = [[0] * (seed_size + 1)]
    seed_world += [[0] + generate_world_row(seed_size) for x in range(seed_size)]
    return inflate_world(seed_world, (seed_size + 1, seed_size + 1))


def quit_callback():
    global done
    done = True


def main():
    global done
    run = False

    # Init pygame
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    world = Grid(WORLD_SIZE)
    world.init_glider()
    clock.tick(1)
    pygame.display.flip()

    # Init tkinter
    root = tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", quit_callback)
    main_dialog = tkinter.Frame(root)
    root.title("Test dialog")
    status_line = tkinter.Label(main_dialog, text="Test String", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
    status_line.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    main_dialog.pack()

    try:
        main_dialog.update()
    except:
        print("dialog error")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                # Pivoted because origin is the top left corner
                target_y = math.floor(pos_x / (margin + c_width))
                target_x = math.floor(pos_y / (margin + c_height))
                world.flip(target_x, target_y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = not run
                if event.key == pygame.K_TAB:
                    world.init_glider()
                if event.key == pygame.K_ESCAPE:
                    world.clear()
                if event.key == pygame.K_g:
                    world.init_glider()
                if event.key == pygame.K_l:
                    world.init_lwss()
                if event.key == pygame.K_m:
                    world.init_mwss()
                if event.key == pygame.K_h:
                    world.init_hwss()

        assert world is not None

        screen.fill(WHITE)
        # See why we put those constraints on the cell sizes and margins? :P
        for i in range(world.size + 1):
            vl_idx = (margin * i) + (c_height * i)
            pygame.draw.line(screen, GREY, [vl_idx + (margin / 2.0), 0], [vl_idx + (margin / 2.0), w_height], margin)
            for j in range(world.size + 1):
                hl_idx = (margin * j) + (c_width * j)
                pygame.draw.line(screen, GREY, [0, hl_idx + (margin / 2.0)], [w_width, hl_idx + (margin / 2.0)], margin)
                color = GREEN if run else RED
                if world.get(i, j):
                    color = BLACK
                pygame.draw.rect(screen, color,
                                 [(margin + c_width) * j + margin,
                                  (margin + c_height) * i + margin,
                                  c_width, c_height])

        if run:
            world.get_next_state()

        clock.tick(6)
        pygame.display.flip()
        try:
            main_dialog.update()
        except:
            print("dialog error")

    pygame.quit()
    main_dialog.destroy()


if __name__ == '__main__':
    main()
