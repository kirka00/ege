from itertools import product

woirds = product('азлопь', repeat=6)
k = 0
for i in woirds:
	word = ''.join(i)
	k += 1
	if word.count('ь') <= 1 and word.count('а') == 1 and word.count('з') <= 2:
		print(k)
		break


# 1599 - true
