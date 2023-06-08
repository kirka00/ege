from itertools import product

k = set()
for i in product('вишня', repeat=6):
	w = ''.join(i)
	if w.count('в') <= 1 and w[0] != 'ш' and w[-1] not in 'ия':
		k.add(w)


print(len(k))


# 4352