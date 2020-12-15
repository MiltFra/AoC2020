nums = map(int, input().split(','))

occs = dict()
last = -1
for t, n in enumerate(nums):
    occs[n] = t
    last = n
    print(f"{t+1}: {n}")
for t in range(len(occs.keys()), 2020):
    n = 0
    if last in occs.keys():
        n = t - 1 - occs[last]
    occs[last] = t - 1
    print(f"{t+1}: {n}")
    last = n