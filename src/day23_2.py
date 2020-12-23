import numpy as np


def normalise(n: int, idx: int):
    return (idx + n) % n


def extract(buf, begin, end):
    begin = normalise(len(buf), begin)
    end = normalise(len(buf), end)
    if begin < end:
        return buf[begin:end]
    else:
        return np.concatenate([buf[begin:], buf[:end]])


# begin < end
def shift_helper(buf, begin, end, dest):
    dest = normalise(len(buf), dest)
    dest_end = normalise(len(buf), dest + end - begin)
    if dest <= dest_end:
        buf[dest:dest_end] = buf[begin:end]
    else:
        d = len(buf) - dest
        buf[dest:dest + d] = buf[begin:begin + d]
        buf[:dest_end] = buf[begin + d:end]


def shift(buf, begin, end, dest):
    begin = normalise(len(buf), begin)
    end = normalise(len(buf), end)
    if begin < end:
        shift_helper(buf, begin, end, dest)
    else:
        shift_helper(buf, begin, len(buf), dest)
        shift_helper(buf, 0, end, dest + len(buf) - begin)


num_iters = 10000000
num_cups = 1000000

cups = dict()

labels = list(map(int, input().strip()))
for a, b in zip(labels[:-1], labels[1:]):
    cups[a] = b

last = labels[-1]
for i in range(len(labels) + 1, num_cups + 1):
    cups[last] = i
    last = i
cups[num_cups] = labels[0]
start = labels[0]
del labels

for k in range(num_iters):
    removed = []
    for _ in range(3):
        removed.append(cups[start])
        cups[start] = cups[cups[start]]
    dest = start
    while (dest := (dest - 2) % num_cups + 1) in removed:
        pass
    old_right = cups[dest]
    cups[dest] = removed[0]
    cups[removed[-1]] = old_right
    start = cups[start]

print(cups[1] * cups[cups[1]])
