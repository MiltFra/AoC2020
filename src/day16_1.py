from sys import stdin
from typing import Tuple
ranges = []

while len(l := input().split()) > 1:
    ab = l[-3].split('-')
    cd = l[-1].split('-')
    ranges.append((int(ab[0]), int(ab[1]), int(cd[0]), int(cd[1])))

valid_values = set()
for (a, b, c, d) in ranges:
    for i in range(a, b + 1):
        valid_values.add(i)
    for i in range(c, d + 1):
        valid_values.add(i)
input()  # your ticket:
my_ticket = list(map(int, input().split(',')))

input()  # empty
input()  # nearby tickets:

tickets = []

for l in stdin:
    tickets.append(list(map(int, l.split(','))))

total = 0
for t in tickets:
    for v in t:
        if not v in valid_values:
            total += v
print(total)
