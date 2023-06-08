from itertools import permutations

k = set()
for i in permutations('мимикрия'):
	w = ''.join(i)
	k.add(w)


print(len(k))


# 3360