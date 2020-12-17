import sys


def count_neighbours(grid, x, y, z, w):
    s = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if grid.get((i, j, k, l), False): s += 1
    if grid.get((x, y, z, w), False):
        s -= 1
    return s


def next_state(grid, x, y, z, w):
    c = count_neighbours(grid, x, y, z, w)
    if grid.get((x, y, z, w), False):
        return 2 <= c <= 3
    else:
        return c == 3


def step(grid, max_x, max_y, i):
    new_grid = dict()
    for x in range(-i - 1, max_x + i + 2):
        for y in range(-i - 1, max_y + i + 2):
            for z in range(-i - 1, i + 2):
                for w in range(-i - 1, i + 2):
                    new_grid[(x, y, z, w)] = next_state(grid, x, y, z, w)
    return new_grid


grid = dict()
max_x, max_y = 0, 0
for i, l in enumerate(sys.stdin):
    for j, c in enumerate(l.strip()):
        grid[(j, i, 0, 0)] = False if c == '.' else True
        max_x = j
    max_y = i

for i in range(6):
    grid = step(grid, max_x, max_y, i)

total = 0
for k in grid.keys():
    if grid[k]:
        total += 1
print(total)
