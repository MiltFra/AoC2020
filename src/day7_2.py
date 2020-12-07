import sys

def get_rule(l):
  s = l.strip().split()
  outer = ' '.join(s[:2])
  if len(s) == 6:
    return (outer, [])
  n = (len(s) // 4) - 1
  inner = []
  for i in range(n):
    loc = s[4*(i+1):4*(i+2)]
    inner.append((' '.join(loc[1:-1]), int(loc[0])))
  return (outer, inner)

rules = []
for l in sys.stdin:
  rules.append(get_rule(l)) 

def get_id(cols, c):
  if idx := cols.get(c, None):
    return idx
  n = len(cols.keys())
  cols[c] = n
  return n

V = { }
E = []
for outer, inners in rules:
  idx1 = get_id(V, outer)
  for inner, count in inners:
    idx2 = get_id(V, inner)
    while len(E) <= idx1:
      E.append([])
    E[idx1].append((idx2, count))
while len(E) < len(V.keys()):
  E.append([])

print(V)

def calculate(V, E, cache, v):
    if v in cache.keys():
      return cache[v]
    total = 1
    for u, k in E[v]:
      total += k * calculate(V, E, cache, u)
    cache[v] = total
    return total
    

print(calculate(V, E, dict(), V['shiny gold'])-1)