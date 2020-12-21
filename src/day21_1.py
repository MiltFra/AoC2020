from sys import stdin

all_ingredients = set()
all_allergens = set()

my_list = []
for l in stdin:
    ps, qs = l.split('(')
    ps = ps.strip().split()
    qs = ' '.join(qs.strip()[:-1].split(' ')[1:]).split(', ')
    print(qs)
    all_ingredients.update(ps)
    all_allergens.update(qs)
    my_list.append((ps, qs))

possible = dict()
for q in all_allergens:
    possible[q] = set(all_ingredients)

for ps, qs in my_list:
    for q in qs:
        possible[q].intersection_update(ps)

free = set(all_ingredients)
contaminated = set()
for q in possible.keys():
    print(q, len(possible[q]), sorted(list(possible[q])))
    contaminated.update(possible[q])
    free.difference_update(possible[q])

total = 0
x = 0
for ps, qs in my_list:
    x += len(ps)
    for p in ps:
        if p in free:
            total += 1
print(len(contaminated), contaminated)
print(total)
