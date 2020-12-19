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


def compile(rules: dict) -> str:
    rxs = [None for _ in range(1+max(rules.keys()))]
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
            rs = [[rxs[r] for r in sub] for sub in rules[e][1]]
            rxs[e] = '(' + '|'.join(map(lambda x: ''.join(x), rs)) + ')'
            stack.pop()
        else:
            rxs[e] = rules[e][1]
    return re.compile("^" + rxs[0] + "$")


rules = dict()
while len(l := input()) > 1:
    read_rule(rules, l)
rx = compile(rules)
count = 0
for l in sys.stdin:
    if re.fullmatch(rx, l.strip()):
        count += 1
print(count)