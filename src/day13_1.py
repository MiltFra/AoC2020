from sys import stdin, exit

target_t = int(input())
closest_t = 0
closest_id = 0

ids = list(map(int, filter(lambda x: x != 'x', input().split(','))))


def get_closest(t, i):
    if t == i:
        return t
    return (1 + t // i) * i - t

for i in ids:
    c = get_closest(target_t, i)
    print(i, c)
    if not closest_id or c < closest_t:
        closest_id = i
        closest_t = c
print(closest_id * closest_t)
