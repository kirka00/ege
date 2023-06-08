from itertools import product

k = 0
for i in product('игрок', repeat=5):
	w = ''.join(i)
	if 'рок' not in w and w[0] != 'к' and w.count('и') == 1 and \
		w.count('г') == 1 and w.count('р') == 1 and \
			w.count('о') == 1 and w.count('к') == 1:
		k += 1


print(k)


# 90