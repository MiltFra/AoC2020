import sys
from math import radians
from cmath import rect

ship_pos = 0 + 0j
orientation = 0

for l in sys.stdin:
    op, val = l[0], int(l[1:])
    if op == 'N': ship_pos += val * 1j
    elif op == 'S': ship_pos -= val * 1j
    elif op == 'E': ship_pos += val
    elif op == 'W': ship_pos -= val
    elif op == 'L': orientation += val
    elif op == 'R': orientation -= val
    elif op == 'F': ship_pos += rect(val, radians(orientation))

print(
    f"p={ship_pos.real:.0f}+{ship_pos.imag:.0f}i, d={abs(ship_pos.real) + abs(ship_pos.imag):.0f}"
)
