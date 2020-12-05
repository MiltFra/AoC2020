import sys


def get_entries():
    raw_entries = []
    for l in sys.stdin:
        if len(l) <= 1:
            break
        raw_entries.extend(l.strip().split())
    if raw_entries == []:
        return
    entries = dict()
    for r in raw_entries:
        k, v = r.split(':')
        entries[k] = v
    return entries


def check_entries(es):
    try:
        x = int(es['byr'])
        if x < 1920 or x > 2002:
            print('Wrong byr', x)
            return False
        x = int(es['iyr'])
        if x < 2010 or x > 2020:
            print('Wrong iyr', x)
            return False
        x = int(es['eyr'])
        if x < 2020 or x > 2030:
            print('Wrong eyr', x)
            return False
        x = es['hgt']
        if x[-2:] == 'cm':
            x = int(x[:-2])
            if x < 150 or x > 193:
                print('Wrong hgt', es['hgt'])
                return False
        elif x[-2:] == 'in':
            x = int(x[:-2])
            if x < 59 or x > 76:
                print('Wrong hgt', es['hgt'])
                return False
        else:
            print('Height missing unit', x)
            return False
        x = es['hcl']
        if x[0] != '#':
            return False
        x = x[1:]
        if not (x.islower() or x.isnumeric()) or not x.isalnum():
            print('Wrong hcl', x, x.islower(), x.isalnum())
            return False
        x = es['ecl']
        if not x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print('Wrong ecl', x)
            return False
        x = es['pid']
        if not x.isnumeric() or len(x) != 9:
            print('Wrong pid', x)
            return False
        return True
    except TypeError:
        print('Type Error')
        return False


required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

valid = 0
while es := get_entries():
    if len(required - es.keys()) == 0:
        if check_entries(es):
            valid += 1
            continue
print(valid)
