import sys
from collections import deque

player1 = deque()
player2 = deque()
input()
while len(l := input()) > 0:
    player1.append(int(l.strip()))
input()
for l in sys.stdin:
    player2.append(int(l.strip()))

while len(player1) and len(player2):
    print(player1, player2)
    a = player1.popleft()
    b = player2.popleft()
    if a > b:
        player1.append(a)
        player1.append(b)
    else:
        player2.append(b)
        player2.append(a)

winner = player1 if len(player1) else player2
score = 0
l = len(winner)
for i, v in enumerate(winner):
    print(f'{score} += {v} * {l - i}')
    score += v * (l - i)
print(score)
