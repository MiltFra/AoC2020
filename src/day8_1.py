import sys

inst_mem = []
for line in sys.stdin:
  args = line.strip().split()
  if len(args) < 2:
    break
  if args[0] == "acc":
    op = 1
  elif args[0] == "jmp":
    op = 2
  else:
    op = 0
  inst_mem.append((op, int(args[1])))

pc = 0
acc = 0
visited = [False for _ in inst_mem]
while True:
  if visited[pc]:
    break
  op, arg = inst_mem[pc]
  visited[pc] = True
  pc += 1
  if not op:
    continue 
  if op == 1:
    acc += arg
  else:
    pc += arg - 1
  
print(acc)
