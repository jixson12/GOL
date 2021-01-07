import math
import random
import pygame
import tkinter

import constants
from grid import Grid
from patterns.stills import *
from patterns.oscillators import *
from patterns.spaceships import *

# Init some colors
BLACK = (0, 0, 0)
GREY = (140, 140, 140)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (200, 255, 200)
YELLOW = (127, 127, 0)
RED = (255, 200, 200)

PATTERNS = {'Glider': Glider, 'LWSS': LWSS, 'MWSS': MWSS, 'HWSS': HWSS,
            'Blinker': Blinker, 'Toad': Toad, 'Beacon': Beacon, 'Pulsar': Pulsar, 'PentaDecathlon': PentaDecathlon,
            'Block': Block, 'Beehive': Beehive, 'Loaf': Loaf, 'Boat': Boat, 'Tub': Tub}

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


def main():
    global BLACK, GREY, WHITE, BLUE, GREEN, YELLOW, RED, WORLD_SIZE, PATTERNS, \
        c_width, c_height, margin, w_width, w_height, size, done
    run = False

    # Init pygame
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    world = Grid(WORLD_SIZE)
    # world.init_glider()

    # Init tkinter
    def quit_callback():
        global done
        done = True

    root = tkinter.Tk()
    root.protocol("WM_DELETE_WINDOW", quit_callback)
    main_dialog = tkinter.Frame(root)
    root.title("Controls of Life")
    dd_var = tkinter.StringVar()
    dd_var.set(list(PATTERNS.keys())[0])
    dropdown = tkinter.OptionMenu(root, dd_var, *PATTERNS.keys())
    dropdown.pack()

    def stop_callback():
        nonlocal run
        print('Stop')
        run = False

    def start_callback():
        nonlocal run
        print('Start')
        run = True

    def place_callback():
        print(f'Place {dd_var.get()}')
        world.init_pattern(PATTERNS[dd_var.get()])

    stop = tkinter.Button(root, text="Stop", command=stop_callback)
    button = tkinter.Button(root, text="Place", command=place_callback)
    start = tkinter.Button(root, text="Start", command=start_callback)
    stop.pack()
    button.pack()
    start.pack()

    main_dialog.pack()
    clock.tick()
    pygame.display.flip()

    try:
        main_dialog.update()
    except:
        print("dialog error")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_callback()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                # Pivoted because origin is the top left corner
                target_y = math.floor(pos_x / (margin + c_width))
                target_x = math.floor(pos_y / (margin + c_height))
                world.flip(target_x, target_y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop_callback() if run else start_callback()
                if event.key == pygame.K_ESCAPE:
                    print('Clear')
                    world.clear()

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
        try:
            main_dialog.update()
        except:
            print("dialog error")

        clock.tick(6)
        pygame.display.flip()

    pygame.quit()
    main_dialog.destroy()


if __name__ == '__main__':
    main()
