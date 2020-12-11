import sys

seats = []
for l in sys.stdin:
  seats.append(['.'])
  seats[-1].extend(list(l.strip()))
  seats[-1].append('.')

W = len(seats[0])-2
H = len(seats)

seats.insert(0, ['.' for _ in range(W+2)])
seats.append(['.' for _ in range(W+2)])


def compare(xs, ys):
  if len(xs) != len(ys):
    return False
  for i in range(len(xs)):
    for j in range(len(xs[i])):
      if xs[i][j] != ys[i][j]:
        return False 
  return True

def update(seats):
  new_seats = [[False for _ in x] for x in seats]
  for x in range(W):
    for y in range(H):
      s = sum(map(lambda x: 1 if x == '#' else 0, [seats[y][x], seats[y][x+1], seats[y][x+2], seats[y+1][x], seats[y+1][x+2], seats[y+2][x], seats[y+2][x+1], seats[y+2][x+2]]))
      if seats[y+1][x+1] == '#':
        new_seats[y+1][x+1] = '#' if s < 4 else 'L'
      elif seats[y+1][x+1] == 'L':
        new_seats[y+1][x+1] = '#' if s == 0 else 'L'
  return new_seats

def count(seats):
  total = 0
  for r in seats:
    for c in r:
      if c == '#':
        total += 1
  return total


old_seats = []
while not compare(seats, old_seats):
  old_seats = seats
  seats = update(seats)
  print(count(seats))
