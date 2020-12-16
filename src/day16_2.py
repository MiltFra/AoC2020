from sys import stdin
from typing import Tuple
ranges = []

while len(l := input().split()) > 1:
    ab = l[-3].split('-')
    cd = l[-1].split('-')
    ranges.append((int(ab[0]), int(ab[1]), int(cd[0]), int(cd[1])))

valid_values = dict()
for i, (a, b, c, d) in enumerate(ranges):
    for j in range(a, b + 1):
        valid_values[j] = valid_values.get(j, []) + [i]
    for j in range(c, d + 1):
        valid_values[j] = valid_values.get(j, []) + [i]
input()  # your ticket:
my_ticket = list(map(int, input().split(',')))

input()  # empty
input()  # nearby tickets:

tickets = []

for l in stdin:
    tickets.append(list(map(int, l.split(','))))

valid_tickets = []
for t in tickets:
    valid = True
    for v in t:
        if not v in valid_values.keys():
            valid = False
            break
    if valid:
        valid_tickets.append(t)

options = [set(range(len(ranges))) for _ in valid_tickets[0]]
for j, t in enumerate(valid_tickets):
    for i, v in enumerate(t):
        if i == 0: print(options[i], valid_values[v])
        options[i].intersection_update(valid_values[v])
        if i == 0: print(options[i], valid_values[v])

n = len(options)
assignment = [-1 for _ in options]
while n:
    removed = set()
    for i, opt in enumerate(options):
        if len(opt) == 1:
            for p in opt:
                assignment[i] = p
                removed.add(p)
                break
    n -= len(removed)
    for opt in options:
        opt.difference_update(removed)
total = 1
print(assignment)
print(my_ticket)
for i, a in enumerate(assignment):
    if a < 6:
        total *= my_ticket[i]
print(total)