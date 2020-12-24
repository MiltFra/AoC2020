import sys


def go_e(p):
    x, y, z = p
    return x + 1, y - 1, z


def go_w(p):
    x, y, z = p
    return x - 1, y + 1, z


def go_ne(p):
    x, y, z = p
    return x + 1, y, z - 1


def go_nw(p):
    x, y, z = p
    return x, y + 1, z - 1


def go_se(p):
    x, y, z = p
    return x, y - 1, z + 1


def go_sw(p):
    x, y, z = p
    return x - 1, y, z + 1


def to_cubic(l):
    p = (0, 0, 0)
    last = ''
    for c in l:
        if c == 's' or c == 'n':
            last = c
            continue
        d = last + c
        last = ''
        if d == 'e':
            p = go_e(p)
        elif d == 'w':
            p = go_w(p)
        elif d == 'ne':
            p = go_ne(p)
        elif d == 'nw':
            p = go_nw(p)
        elif d == 'se':
            p = go_se(p)
        elif d == 'sw':
            p = go_sw(p)
    return p


floor = dict()
for l in sys.stdin:
    c = to_cubic(l.strip())
    floor[c] = not floor.get(c, False)

iters = 100
for _ in range(iters):
    new_floor = dict()
    ns = dict()
    for k in floor.keys():
        if floor[k]:
            p = go_e(k)
            ns[p] = ns.get(p, 0) + 1
            p = go_w(k)
            ns[p] = ns.get(p, 0) + 1
            p = go_ne(k)
            ns[p] = ns.get(p, 0) + 1
            p = go_nw(k)
            ns[p] = ns.get(p, 0) + 1
            p = go_se(k)
            ns[p] = ns.get(p, 0) + 1
            p = go_sw(k)
            ns[p] = ns.get(p, 0) + 1
    for k in ns.keys():
        if floor.get(k, False):
            if 0 < ns[k] <= 2:
                new_floor[k] = True
        else:
            if ns[k] == 2:
                new_floor[k] = True
    floor = new_floor

total = 0
for k in floor.keys():
    if floor[k]:
        total += 1
print(total)
