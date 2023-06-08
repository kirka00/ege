from itertools import product

k = 0
for i in product('сало', repeat=6):
	w = ''.join(i)
	if 1 <= w.count('о') <= 3:
		k += 1


print(k)


# 3213