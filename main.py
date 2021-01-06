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
