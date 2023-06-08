from itertools import product

k = set()
for i in product('abcd', repeat=4):
	w = ''.join(i)
	if ''.join(sorted(w)) == w:
		k.add(w)


print(len(k))


# 35