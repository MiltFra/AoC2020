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

ns = {i:0 for i in range(1 << 10)}
for line in sys.stdin:
  sid = seatid(line)
  ns[sid] += 4
  ns[sid-1] += 1
  ns[sid+1] += 2
  print(sid, ns[sid])
for i in ns:
  if ns[i] == 3:
    print(i)
    break