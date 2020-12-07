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
    inner.append(' '.join(loc[1:-1]))
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
  for inner in inners:
    idx0 = get_id(V, inner)
    while len(E) <= idx0:
      E.append([])
    E[idx0].append(idx1)
while len(E) < len(V.keys()):
  E.append([])

print(V)

visited = [False for _ in range(len(V.keys()))]
to_visit = [V['shiny gold']]
count = 0
while len(to_visit):
  v = to_visit.pop()
  if visited[v]:
    continue
  visited[v] = True
  count += 1
  to_visit.extend(E[v])

print(count - 1)