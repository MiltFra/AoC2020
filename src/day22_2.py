import sys
from collections import deque
import hashlib


def hash(player):
    s = 0
    f = 1
    for p in player:
        s += p * f
        f <<= 1
    return s


next_i = 1


def play(player1: deque, player2: deque):
    global next_i
    i = next_i
    next_i += 1
    full_seen = set()
    j = 1
    while len(player1) and len(player2):
        #print(f"Player 1's deck: {', '.join(map(str, player1))}")
        #print(f"Player 2's deck: {', '.join(map(str, player2))}")
        h1, h2 = hash(player1), hash(player2)
        if (h1, h2) in full_seen:
            return (True, player1)
        full_seen.add((h1, h2))
        a = player1.popleft()
        b = player2.popleft()
        #print(f"Player 1 plays: {a}")
        #print(f"Player 2 plays: {b}")
        if a <= len(player1) and b <= len(player2):
            a_wins, _ = play(deque(list(player1)[:a]),
                             deque(list(player2)[:b]))
        else:
            a_wins = a > b
        if a_wins:
            #print(f"Player 1 wins round {j} of game {i}!")
            player1.append(a)
            player1.append(b)
        else:
            #print(f"Player 2 wins round {j} of game {i}!")
            player2.append(b)
            player2.append(a)
        j += 1
    if not len(player1):
        #print(f"Player 1 wins game {i}!")
        return (False, player2)
    elif not len(player2):
        return (True, player1)


player1 = deque()
player2 = deque()
input()
while len(l := input()) > 0:
    player1.append(int(l.strip()))
input()
for l in sys.stdin:
    player2.append(int(l.strip()))

a_won, winner = play(player1, player2)
print(winner)
score = 0
l = len(winner)
for i, v in enumerate(winner):
    score += v * (l - i)
print(score)
