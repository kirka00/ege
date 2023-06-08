from itertools import product

k = 0
for i in product('лодка', repeat=4):
	w = ''.join(i)
	if w.count('о') >= 2:
		k += 1

print(k)


# 113