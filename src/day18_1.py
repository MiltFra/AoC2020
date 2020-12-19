import sys


def apply(e, cur):
    v, op = e
    if op:
        return v * cur
    else:
        return v + cur


def evaluate(expr):
    expr = ''.join(expr.strip().split())
    stack = [(0, 0)]  # (NUM, OP)
    cur = 0
    for i, c in enumerate(expr):
        if c == '(':
            stack.append((0, 0))
        elif c.isnumeric():
            cur *= 10
            cur += ord(c) - ord('0')
        elif c == '+':
            stack[-1] = (apply(stack[-1], cur), 0)
            cur = 0
        elif c == '*':
            stack[-1] = (apply(stack[-1], cur), 1)
            cur = 0
        elif c == ')':
            cur = apply(stack.pop(), cur)
    return apply(stack.pop(), cur)

total = 0
for l in sys.stdin:
    total += evaluate(l)
print(total)