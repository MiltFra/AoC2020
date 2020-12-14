from sys import stdin, exit

input()

ids = list(map(lambda x: 0 if x == 'x' else int(x), input().split(',')))
table = dict()

constraints = []
for i, x in enumerate(ids):
    if x != 0:
        constraints.append((x, i))
constraints.sort(key=lambda x: x[0], reverse=True)

m = ids[0]
for i in range(m):
    for j in range(m):
        v = (i * j) % m
        while (i, v) not in table.keys():
            table[(i, v)] = j


def get_closest(t, i):
    if t == i:
        return t
    return (1 + t // i) * i - t


def next(t, m, x, i):
    while (t - i) % m:
        t += x
    return t


step = constraints[0][0]
offset = constraints[0][1]
t = 0

while True:
    t = next(t + step, m, step, offset)
    valid = True
    for x, o in constraints[1:]:
        if (t - offset + o) % x != 0:
            valid = False
            break
    if valid:
        print(t - offset)
        exit(0)
