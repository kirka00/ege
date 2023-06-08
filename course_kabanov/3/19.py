from itertools import product

k = 0
for i in product('аимря', repeat=4):
	w = ''.join(i)
	k += 1
	if w == 'ария':
		print(k)
		break




# 85