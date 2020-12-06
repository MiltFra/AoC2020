import sys

count = 0
group = set()
for l in sys.stdin:
  if len(l) <= 1:
    count += len(group)
    group = set()
  else:
    group.update(l.strip())
count += len(group)
print(count)