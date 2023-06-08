from itertools import product

k = 0
for i in product('пуля', repeat=6):
	w = ''.join(i)
	if w.count('у') == 2:
		k += 1

print(k)


# 1215