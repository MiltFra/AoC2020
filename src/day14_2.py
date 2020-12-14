from sys import stdin


def to_list(x):
    l = []
    for _ in range(36):
        l.append(x & 1)
        x >>= 1
    l.reverse()
    return l


def apply(mask, addr):
    addr_list = to_list(addr)
    base = 0
    free = []
    for i in range(36):
        base <<= 1
        if mask[i] == None:
            free.append(1 << (35 - i))
        else:
            base += mask[i] | addr_list[i]
    return (base, free)


def make_mask(s):
    return list(map(lambda x: int(x) if x != 'X' else None, s))

def calculate(base, free, p):
    for i in range(len(free)):
        if p & 1:
            base += free[i]
        p >>= 1
    return base


mem = dict()
mask = 0
for l in stdin:
    a, b = l.split('=')
    if a[1] == 'e':  # mem
        a = int(a[4:-2])
        b = int(b)
        base, free = apply(mask, a)
        for i in range(1 << len(free)):
            mem[calculate(base, free, i)] = b
    else:  #mask
        mask = make_mask(b.strip())
s = sum(mem.values())
print(s)
