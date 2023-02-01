from itertools import product

k = set()
words = product('0123', repeat=3)
for i in words:
	s = ''.join(i)
	if s != sorted(s):
		k.add(s)


print(len(k))
