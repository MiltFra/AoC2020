import re
import sys


def read_rule(rules: dict, l: str):
    s = l.split(':')
    i = int(s[0])
    l = s[1].strip()
    if l[0] == '"':  # "a"
        rules[i] = (0, l[1])
        return
    rules[i] = (1, [list(map(int, r.strip().split())) for r in l.split('|')])


def compile(rules: dict, max_len: int) -> str:
    rxs = [None for _ in range(1 + max(rules.keys()))]
    stack = [0]
    while len(stack) > 0:
        e = stack[-1]
        if rxs[e]:
            stack.pop()
            continue
        if rules[e][0]:
            prepared = True
            for sub in rules[e][1]:
                for r in sub:
                    if not rxs[r]:
                        prepared = False
                        stack.append(r)
            if not prepared:
                continue
            if e == 11:
                a, b = rules[e][1][0]  # [42, 31]
                r = []
                r = [r := [a] + r + [b] for _ in range(max_len // 2)]
                rules[e] = (1, r)
            rs = [[rxs[r] for r in sub] for sub in rules[e][1]]
            f = lambda x: '(' + x + ')'
            rxs[e] = f('|'.join(map(lambda x: ''.join(x), rs)))
            if e == 8:
                rxs[e] = rxs[e] + '+'
            stack.pop()
        else:
            rxs[e] = rules[e][1]
    return re.compile("^" + rxs[0] + "$")


rules = dict()
while len(l := input()) > 1:
    read_rule(rules, l)
ins = []
for l in sys.stdin:
    ins.append(l.strip())
max_len = max(map(len, ins))
rx = compile(rules, max_len)
count = 0
for l in ins:
    if re.fullmatch(rx, l):
        count += 1
print(count)