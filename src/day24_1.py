import sys


def to_cubic(l):
    x, y, z = 0, 0, 0
    last = ''
    for c in l:
        if c == 's' or c == 'n':
            last = c
            continue
        d = last + c
        last = ''
        if d == 'e':
            x += 1
            y -= 1
        elif d == 'w':
            x -= 1
            y += 1
        elif d == 'ne':
            x += 1
            z -= 1
        elif d == 'nw':
            y += 1
            z -= 1
        elif d == 'se':
            y -= 1
            z += 1
        elif d == 'sw':
            x -= 1
            z += 1
    return (x, y, z)


floor = dict()
for l in sys.stdin:
    c = to_cubic(l.strip())
    floor[c] = not floor.get(c, False)

total = 0
for k in floor.keys():
    if floor[k]:
        total += 1
print(total)
