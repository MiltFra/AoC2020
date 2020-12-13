import sys
from math import radians
from cmath import rect

pos = 0 + 0j
theta = 0

for l in sys.stdin:
    op, val = l[0], int(l[1:])
    if op == 'N': pos += val * 1j
    elif op == 'S': pos -= val * 1j
    elif op == 'E': pos += val
    elif op == 'W': pos -= val
    elif op == 'L': theta += val
    elif op == 'R': theta -= val
    elif op == 'F': pos += rect(val, radians(theta))

print(
    f"p={pos.real:.0f}+{pos.imag:.0f}i, d={abs(pos.real) + abs(pos.imag):.0f}"
)
