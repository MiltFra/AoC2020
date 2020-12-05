import os
import sys

dx, dy = 3, 1

m = []
count = 0

for l in sys.stdin:
    m.append(l.strip())

x, y = 0, 0
while y < len(m)-dy:
    x += dx
    y += dy
    if m[y][x % len(m[y])] == '#':
        count += 1
print(count)
