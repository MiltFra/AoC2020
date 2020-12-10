import sys

def note_ways(adapts, ways, i):
  j = i + 1
  while j < len(adapts) and adapts[j] - 3 <= adapts[i]: 
    ways[j] += ways[i]
    j += 1

adapts = sorted([int(l) for l in sys.stdin])
adapts.append(adapts[-1]+3)
adapts.insert(0, 0)

ways = [0 for _ in adapts]
ways[0] = 1
for i in range(len(adapts)):
  note_ways(adapts, ways, i)
print(ways[-1])
