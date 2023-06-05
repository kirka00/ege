from itertools import permutations

k = set()
for i in permutations('парабола'):
	w = ''.join(i)
	s = ''
	for c in w:
		if c in 'ао':
			s += 'g'
		else:
			s += 's'
	if 'gg' not in s and 'ss' not in s:
		k.add(w)
print(len(k))


# 192