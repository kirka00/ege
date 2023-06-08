from itertools import product

k = set()
for i in product('0123456789', repeat=3):
	w = ''.join(i)
	if ''.join(sorted(w)) == w and w[0] != '0':
		k.add(w)


print(len(k))


# 35