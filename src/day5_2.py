import sys

def extend_sid(sid, s, c0):
  for c1 in s:
    sid <<= 1
    if c0 == c1:
      sid += 1
  return sid

def seatid(bsp):
  sid = extend_sid(0, bsp[:7], 'B')
  sid = extend_sid(sid, bsp[7:10], 'R')
  return sid

ns = [0 for _ in range(1 << 10)]
for line in sys.stdin:
  sid = seatid(line)
  ns[sid] += 4
  if sid - 1 > 0:
    ns[sid-1] += 1
  if sid + 1 < len(ns):
    ns[sid+1] += 2
for i, n in enumerate(ns):
  if n == 3:
    print(i)
    break