import sys

P = 25

# Initial preamble
preamble_start = 0
preamble = [int(input()) for _ in range(P)]

def translate_index(x):
  return (preamble_start + x) % P

def write_preamble(i, v):
  preamble[translate_index(i)] = v

def read_preamble(i):
  return preamble[translate_index(i)]

# Initial sums
sums_in_preamble = dict()

def update_sums(x, d):
  sums_in_preamble[x] = sums_in_preamble.get(x, 0) + d

def is_valid_sum(x):
  return sums_in_preamble.get(x, 0)

for i in range(P):
  for j in range(i):
    update_sums(read_preamble(i)+read_preamble(j), 1)

# Check whether an x is valid and update preamble and sums
def check(x):
  global preamble_start
  if not is_valid_sum(x): # O(1)
    print(x)
    return False
  old_x = read_preamble(0) 
  for i in range(1,P): # O(P)
    y = read_preamble(i)
    update_sums(old_x+y, -1)
    update_sums(x+y, 1)
  # Move circular buffer around.
  write_preamble(0, x)
  preamble_start = (preamble_start + 1) % P
  return True

# Step through other N-P elements
for l in sys.stdin: # N - P times, so it's O(N*P)
  x = int(l.strip())
  if not check(x): # O(P)
    break

