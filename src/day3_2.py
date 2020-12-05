import os
import sys


def get_map():
    m = []
    for l in sys.stdin:
        m.append(l.strip())
    return m


def check_slope(m, dx, dy):
    x, y = 0, 0
    count = 0
    while y < len(m)-dy:
        x += dx
        y += dy
        if m[y][x % len(m[y])] == '#':
            count += 1
    return count


m = get_map()
ds = [(1, 1), (3, 1), (5, 1), (7, 1),(1, 2)]
output = 1
for dx, dy in ds:
    output *= check_slope(m, dx, dy)


print(output)
