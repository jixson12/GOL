import math
import random
import pygame
import tkinter as tk

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
    shadow_world = Grid(WORLD_SIZE, shadow=True)
    # world.init_glider()

    # Init tk
    def quit_callback():
        global done
        done = True

    def stop_callback():
        nonlocal run
        print('Stop')
        run = False

    def start_callback():
        nonlocal run
        print('Start')
        run = True

    def place_callback():
        nonlocal pat_var, x_var, y_var, flip_var, deg_var
        pattern = pat_var.get()
        x_ofst = int(x_var.get())
        y_ofst = int(y_var.get())
        flipped = flip_var.get()
        degrees = deg_var.get()
        print(f'Place {pattern} at offset ({x_ofst}:{y_ofst}); rotation {degrees}; flipped {flipped}')
        world.init_pattern(PATTERNS[pat_var.get()], x_offset=(WORLD_SIZE / 2) + x_ofst,
                           y_offset=(WORLD_SIZE / 2) + y_ofst, rotation=degrees, flipped=flipped)

    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", quit_callback)
    root.title("Controls of Life")

    main_dialog = tk.Frame(root)
    tk.Label(main_dialog, text='X:').grid(row=0, column=0)
    x_var = tk.StringVar()
    x_field = tk.Entry(main_dialog, width=3, textvariable=x_var)
    x_field.insert(0, 0)
    x_field.grid(row=0, column=1)
    tk.Label(main_dialog, text='Y:').grid(row=0, column=2)
    y_var = tk.StringVar()
    y_field = tk.Entry(main_dialog, width=3, textvariable=y_var)
    y_field.insert(0, 0)
    y_field.grid(row=0, column=3)

    flip_var = tk.BooleanVar()
    flip_var.set(False)
    flip_radio = tk.Checkbutton(main_dialog, text='Flipped', variable=flip_var)
    flip_radio.grid(row=0, column=4)

    tk.Label(main_dialog, text='Pattern: ').grid(row=1, column=0)
    pat_var = tk.StringVar()
    pat_var.set(list(PATTERNS.keys())[0])
    pat_dd = tk.OptionMenu(main_dialog, pat_var, *PATTERNS.keys())
    pat_dd.grid(row=1, column=1)
    deg_var = tk.StringVar()
    deg_var.set('0')
    deg_dd = tk.OptionMenu(main_dialog, deg_var, '0', '90', '180', '270')
    deg_dd.grid(row=1, column=2)
    tk.Label(main_dialog, text='degrees').grid(row=1, column=3)

    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, side=tk.BOTTOM)
    stop = tk.Button(button_frame, text="Stop", command=stop_callback)
    button = tk.Button(button_frame, text="Place", command=place_callback)
    start = tk.Button(button_frame, text="Start", command=start_callback)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=2)
    button_frame.columnconfigure(2, weight=1)
    stop.grid(row=2, column=0, sticky=tk.W+tk.E)
    button.grid(row=2, column=1, sticky=tk.W+tk.E)
    start.grid(row=2, column=2, sticky=tk.W+tk.E)
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
                target_x = math.floor(pos_x / (margin + c_width))
                target_y = math.floor(pos_y / (margin + c_height))
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
                if i == WORLD_SIZE / 2 or j == WORLD_SIZE / 2:
                    color = WHITE
                if world.get(i, j):
                    color = BLACK
                if shadow_world.get(i, j):
                    shade = 6 - shadow_world.get(i, j)
                    color = (shade * 50, shade * 50, shade * 50)
                pygame.draw.rect(screen, color,
                                 [(margin + c_width) * i + margin,
                                  (margin + c_height) * j + margin,
                                  c_width, c_height])

        if run:
            world.get_next_state(shadow_world)
        try:
            main_dialog.update()
        except:
            print("dialog error")

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    main_dialog.destroy()


if __name__ == '__main__':
    main()
