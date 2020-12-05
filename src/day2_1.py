def getline():
    try:
        return input()
    except EOFError:
        return None


def check(pw, a, b, c):
    print(pw, a, b, c)
    count = 0
    for x in pw:
        if x == c:
            count += 1
    return count >= a and count <= b


valid = 0
while l := getline():
    s = l.split()
    a, b = map(int, s[0].split('-'))
    c = s[1][0]
    pw = s[2]
    if check(pw, a, b, c):
        valid += 1
print(valid)
