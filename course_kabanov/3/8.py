from itertools import product

k = set()
for i in product('ab123', repeat=8):
	w = ''.join(i)
	if w.count('a') + w.count('b') == 2 and \
		w.count('1') + w.count('2') + w.count('3') == 2:
		k.add(w)


print(len(k))


# 81648