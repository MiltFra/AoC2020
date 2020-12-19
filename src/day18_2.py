import sys


def apply(e, cur):
    v, op = e
    if op:
        return v * cur
    else:
        return v + cur


def evaluate(expr):
    expr = ''.join(expr.strip().split())
    expr += ')'
    stack = [0, '+', '(']
    cur = 0
    for i, c in enumerate(expr):
        if c == '*' or c == '+':
            if stack[-1] == '+':
                stack.pop()
                cur += stack.pop()
            stack.append(cur)
            stack.append(c)
            cur = 0
        elif c.isnumeric():
            cur *= 10
            cur += ord(c) - ord('0')
        elif c == '(':
            stack.append(c)
        elif c == ')':
            if stack[-1] == '+':
                stack.pop()
                cur += stack.pop()
            while (p := stack.pop()) != '(':
                if p != '*':
                    cur *= p
            if stack[-1] == '+':
                stack.pop()
                cur += stack.pop()
    return cur

total = 0
for l in sys.stdin:
    total += evaluate(l)
print(total)