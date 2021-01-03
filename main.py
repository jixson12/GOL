import math
import random
import pygame

BLACK = (0, 0, 0)
GREY = (120, 120, 120)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (127, 127, 0)
RED = (255, 0, 0)
WORLD_SIZE = 21
assert WORLD_SIZE >= 4
c_width = c_height = 20
margin = 5
w_width = (c_width * WORLD_SIZE) + (margin * (WORLD_SIZE + 1))
w_height = (c_height * WORLD_SIZE) + (margin * (WORLD_SIZE + 1))
size = (w_width, w_height)


init_world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def generate_world_row():
    global WORLD_SIZE
    return [round(random.random()) for x in range(WORLD_SIZE)]


def get_next_state(world):
    global WORLD_SIZE
    new_state = [[0] * WORLD_SIZE for x in range(WORLD_SIZE)]
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            neighbors = get_neighbors_set(i, j)
            live_neighbors = 0
            for n in neighbors:
                live_neighbors += world[n[0]][n[1]]
            if not world[i][j] and live_neighbors == 3:
                new_state[i][j] = 1
            elif world[i][j] and 2 <= live_neighbors <= 3:
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


pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
done = False
run = False
clock = pygame.time.Clock()
world = init_world if init_world else [generate_world_row() for x in range(WORLD_SIZE)]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            target_x = math.floor(pos_x / (margin + c_width))
            target_y = math.floor(pos_y / (margin + c_height))
            world[target_y][target_x] = math.fabs(world[target_y][target_x] - 1)
            print(f'Clicked pos {pos_x}:{pos_y} which should be cell ({target_x}, {target_y})')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = not run
            if event.key == pygame.K_TAB:
                world = init_world

    screen.fill(WHITE)
    for i in range(WORLD_SIZE):
        vl_idx = (margin * i) + (c_height * i)
        pygame.draw.line(screen, GREY, [vl_idx, 0], [vl_idx, w_height - 1], 5)
        for j in range(WORLD_SIZE):
            hl_idx = (margin * j) + (c_width * j)
            pygame.draw.line(screen, GREY, [0, hl_idx], [w_width - 1, hl_idx], 5)
            color = WHITE
            if world[i][j] == 1:
                print(f'{i}:{j} - {get_neighbors_set(i, j)}')
                color = BLACK
            pygame.draw.rect(screen, color,
                             [(margin + c_width) * j + margin,
                              (margin + c_height) * i + margin,
                              c_width, c_height])
    clock.tick(4)
    pygame.display.flip()
    if run:
        new_world = get_next_state(world)
        world = new_world

pygame.quit()
