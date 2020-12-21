from collections import Counter


def encode(digits):
    total = 0
    for d in digits:
        total <<= 1
        total += d
    return total


def flip(n):
    new_n = 0
    for _ in range(10):
        new_n <<= 1
        new_n += n & 1
        n >>= 1
    return new_n


def process_tile():
    f = lambda x: 1 if x == '#' else 0
    try:
        l = input().strip()
    except EOFError:
        return None
    x = int(l.split()[1][:-1])
    l = input().strip()
    top = map(f, l)
    left = [f(l[0])]
    right = [f(l[-1])]
    for _ in range(9):
        l = input().strip()
        left.append(f(l[0]))
        right.append(f(l[-1]))
    bottom = reversed(list(map(f, l)))
    left.reverse()
    input()
    return (x, [encode(top), encode(left), encode(bottom), encode(right)])


tiles = []
vs = Counter()
while t := process_tile():
    tiles.append(t)
    vs.update(t[1])
    vs.update(map(flip, t[1]))

corners = []
for t in tiles:
    p = 0
    for v in t[1]:
        if vs.get(v) == 1:
            p += 1
    if p == 2:
        corners.append(t[0])

total = 1
for c in corners:
    total *= c

print(len(tiles))
print(corners)
print(total)
