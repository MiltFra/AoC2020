import heapq
xs = []
output = None
while output == None:
    y = int(input())
    print(y)
    for x in xs:
      if x + y == 2020:
        output = x *y 
        break
    xs.append(y)
print(output)
