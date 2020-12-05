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

hi = 0
for line in sys.stdin:
  sid = seatid(line)
  hi = max(hi, sid) 
print(hi)