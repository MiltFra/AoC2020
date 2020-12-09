import sys
from collections import deque

def check(preamble, x):
  s = set(preamble)
  for y in s:
    if x - y in s:
      preamble.append(x)
      preamble.popleft()
      return True
  return False

def find_k(nums):
  p = deque(nums[:25])
  for x in nums[25:]:
    if not check(p, x):
      return x
  return None



nums = []

for l in sys.stdin:
  x = int(l.strip())
  nums.append(x)

k = find_k(nums)

a,b = 0, 0
while True:
  s = sum(nums[a:b])
  if s == k:
    print(max(nums[a:b])+min(nums[a:b]))
    break
  if s < k:
    b += 1
  elif s > k:
    a += 1
