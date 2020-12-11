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

def f(seats, x, y):
  c = seats[y+1][x+1]
  if c == 'L':
    return 0
  if c == '#':
    return 1
  return None

def count_neighs(seats, x, y):
  if seats[y+1][x+1] == '.':
    return 0
  s = 0
  up = x+1
  down = len(seats[0])-2-x
  left = y+1
  right = len(seats)-2-y
  # Up
  for d in range(1, up):
    if (c := f(seats, x-d, y)) != None:
      s += c
      break
  # Left
  for d in range(1, left):
    if (c := f(seats, x, y-d)) != None:
      s += c
      break
  # Down
  for d in range(1,down):
    if (c := f(seats, x+d, y)) != None:
      s += c
      break
  # Right
  for d in range(1, right):
    if (c := f(seats, x, y+d)) != None:
      s += c
      break
  # UL
  for d in range(1, min(up, left)):
    if (c := f(seats, x-d, y-d)) != None:
      s += c
      break
  # UR
  for d in range(1, min(up, right)):
    if (c := f(seats, x-d, y+d)) != None:
      s += c
      break
  # DL
  for d in range(1, min(down, left)):
    if (c := f(seats, x+d, y-d)) != None:
      s += c
      break
  # DR
  for d in range(1, min(down, right)):
    if (c := f(seats, x+d, y+d)) != None:
      s += c
      break
  return s

   
def update(seats):
  new_seats = [[False for _ in x] for x in seats]
  for x in range(W):
    for y in range(H):
      s = count_neighs(seats, x, y)
      if seats[y+1][x+1] == '#':
        new_seats[y+1][x+1] = '#' if s < 5 else 'L'
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
