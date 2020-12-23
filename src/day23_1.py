import sys


def normalise(buf, idx):
    return (idx + len(buf)) % len(buf)


def move(buf, src, dest):
    src = normalise(buf, src)
    dest = normalise(buf, dest)
    buf[dest] = buf[src]


def extract(buf, begin, end):
    begin = normalise(buf, begin)
    end = normalise(buf, end)
    if begin < end:
        return buf[begin:end]
    else:
        return buf[begin:] + buf[:end]


def shift(buf, begin, end, dest):
    begin = normalise(buf, begin)
    end = normalise(buf, end)
    dest = normalise(buf, dest)
    r = range(begin, end) if begin < end else list(range(
        begin, len(buf))) + list(range(end))
    for src in r:
        move(buf, src, dest)
        dest = normalise(buf, dest + 1)


labels = list(map(int, input().strip()))
present = [True for _ in labels]

src = 0

for _ in range(100):
    pick_up = extract(labels, src + 1, src + 4)
    dest = ((labels[src] - 2) % len(labels)) + 1
    while dest in pick_up:
        dest = ((dest - 2) % len(labels)) + 1
    dest = labels.index(dest)
    print(src, dest, labels)
    shift(labels, src + 4, dest + 1, src + 1)
    dest = normalise(labels, dest - 3)
    for i in range(3):
        dest = normalise(labels, dest + 1)
        labels[dest] = pick_up[i]
    src = normalise(labels, src + 1)

idx = labels.index(1)
print(''.join(map(str, labels[idx:] + labels[:idx]))[1:])