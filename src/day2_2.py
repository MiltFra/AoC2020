def getline():
    try:
        return input()
    except EOFError:
        return None


def check(pw, a, b, c):
    print(pw, a, b, c)
    if a > len(pw) or b > len(pw):
        return False
    return (pw[a-1] == c) != (pw[b-1] == c)


valid = 0
while l := getline():
    s = l.split()
    a, b = map(int, s[0].split('-'))
    c = s[1][0]
    pw = s[2]
    if check(pw, a, b, c):
        valid += 1
print(valid)
