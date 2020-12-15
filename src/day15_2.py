NUM = 30000000
nums = map(int, input().split(','))

occs = dict()
last = -1
for t, n in enumerate(nums):
    occs[n] = t
    last = n
for t in range(len(occs.keys()), NUM):
    n = 0
    if last in occs.keys():
        n = t - 1 - occs[last]
    occs[last] = t - 1
    last = n
print(last)