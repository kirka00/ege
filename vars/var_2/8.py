from itertools import product
stek = product('0123', repeat=5)

k = set()
for i in stek:
	n = ''.join(i)
	if n.count('3') == 1 and n[0] != '0' and '03' not in n \
		and '30' not in n:
		k.add(i)
print(len(k))


# true
