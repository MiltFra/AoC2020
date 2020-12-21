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
for q in possible.keys():
    print(q, len(possible[q]), sorted(list(possible[q])))
    free.difference_update(possible[q])

contained_in = dict()
for _ in range(len(all_allergens)):
    the_p, the_q = None, None
    for q in all_allergens:
        if len(possible[q]) == 1:
            the_q = q
            for p in possible[q]:
                the_p = p
            break
    contained_in[the_q] = the_p
    for q2 in all_allergens:
        possible[q2].difference_update([the_p])
print(','.join(map(lambda x: x[1],
    sorted([(k, contained_in[k]) for k in contained_in.keys()],
           key=lambda x: x[0]))))
