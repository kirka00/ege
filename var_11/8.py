from itertools import product

k = set()
words = product('0123', repeat=3)
for i in words:
	s = ''.join(i)
	if s[0] > s[1] > s[2]:
		k.add(s)


print(len(k))

# 4 - true
