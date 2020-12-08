import sys

inst_mem = []
for line in sys.stdin:
  args = line.strip().split()
  if len(args) < 2:
    break
  if args[0] == "acc":
    op = 2
  elif args[0] == "jmp":
    op = 1
  else:
    op = 0
  inst_mem.append([op, int(args[1])])

def check_loop(mem):
  pc = 0
  acc = 0
  visited = [False for _ in inst_mem]
  while True:
    if pc >= len(mem):
      return acc
    if visited[pc]:
      return None
    op, arg = inst_mem[pc]
    visited[pc] = True
    pc += 1
    if not op:
      continue 
    if op == 2:
      acc += arg
    else:
      pc += arg - 1

for i in range(len(inst_mem)):
  if inst_mem[i][0] == 2:
    continue
  inst_mem[i][0] = 1-inst_mem[i][0]
  v = check_loop(inst_mem)
  if v != None:
    print(v)
    break
  inst_mem[i][0] = 1-inst_mem[i][0]