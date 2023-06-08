from itertools import product

k = 0
for i in product('агилморт', repeat=4):
	w = ''.join(i)
	k += 1
	if w == 'ттим':
		print(k)
		break




# 4053