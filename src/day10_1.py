import sys

adapts = sorted([int(l) for l in sys.stdin])
adapts.append(adapts[-1]+3)

last = 0
diffs = dict()
for a in adapts:
  d = a - last
  diffs[d] = diffs.get(d, 0) + 1
  last = a
print(diffs)
print(diffs[1]*diffs[3])