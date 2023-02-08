from itertools import product

words = product('кнорся', repeat=6)
k = 0
for w in words:
	k += 1
	if w.count('к') <= 3 and w.count('я') == 2:
		print(k)
		break


# 72 - true
