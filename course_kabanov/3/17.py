from itertools import product

k = 0
for i in product('елмру', repeat=4):
	w = ''.join(i)
	k += 1
	if w[0] == 'л':
		print(k)
		break




# 126