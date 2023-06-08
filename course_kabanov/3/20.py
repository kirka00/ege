from itertools import product

k = 0
for i in product('аимря', repeat=4):
	w = ''.join(i)
	k += 1
	if k == 211:
		print(w)
		break




# ирма (большими буквами)