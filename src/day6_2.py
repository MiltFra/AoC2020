import sys

def make_group():
  return set([chr(c) for c in range(ord('a'), ord('z')+1)])

count = 0
group = make_group()
for l in sys.stdin:
  if len(l) <= 1:
    count += len(group)
    group = make_group()
  else:
    group = group.intersection(l.strip())
print(count)