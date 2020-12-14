from sys import stdin


def apply(mask, new):
    new_list = []
    for _ in range(36):
        new_list.append(new & 1)
        new >>= 1
    new_list.reverse()
    out = 0
    for x, y in zip(mask, new_list):
        out <<= 1
        if x == None:
            out += y
        else:
            out += x
    return out


def make_mask(s):
    return list(map(lambda x: int(x) if x != 'X' else None, s))


mem = dict()
mask = 0
for l in stdin:
    a, b = l.split('=')
    if a[1] == 'e':  # mem
        a = int(a[4:-2])
        b = int(b)
        mem[a] = apply(mask, b)
    else:  #mask
        mask = make_mask(b.strip())
s = sum(mem.values())
print(s)
