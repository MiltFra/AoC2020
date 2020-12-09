import sys
from collections import deque

preamble = deque()
for _ in range(25):
  preamble.append(int(input()))

def check(preamble, x):
  s = set(preamble)
  for y in s:
    if x - y in s:
      preamble.append(x)
      preamble.popleft()
      return True
  return False

for l in sys.stdin:
  x = int(l.strip())
  if not check(preamble, x):
    print(x)
    break
