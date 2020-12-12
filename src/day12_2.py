import sys
from math import radians
from cmath import rect

ship_pos = 0 + 0j
wp_pos = 10 + 1j

for l in sys.stdin:
    op, val = l[0], int(l[1:])
    if op == 'N': wp_pos += val * 1j
    elif op == 'S': wp_pos -= val * 1j
    elif op == 'E': wp_pos += val
    elif op == 'W': wp_pos -= val
    elif op == 'L': wp_pos *= rect(1, radians(val))
    elif op == 'R': wp_pos *= rect(1, radians(-val))
    elif op == 'F': ship_pos += val * wp_pos

print(
    f"p={ship_pos.real:.0f}+{ship_pos.imag:.0f}i, d={abs(ship_pos.real) + abs(ship_pos.imag):.0f}"
)
