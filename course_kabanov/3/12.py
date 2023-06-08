from itertools import product

k = set()
for i in product('гепард', repeat=5):
	w = ''.join(i)
	if w.count('г') == 1 and w[0] != 'а' and w[-1] != 'е':
		k.add(w)


print(len(k))


# 2200