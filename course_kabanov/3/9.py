from itertools import product

k = set()
for i in product('01234', repeat=6):
	w = ''.join(i)
	if w[-1] != '3' and w[-1] != '4' and w[0] != '1' and w[0] != '0':
		k.add(w)


print(len(k))


# 5625