import heapq
vals = []
output = None
while output == None:
    z = int(input())
    print(z)
    for x in vals:
        for y in vals:
            if x + y + z == 2020:
                output = x * y * z
                break
    vals.append(z)
print(output)
