from itertools import permutations

k = 0
for i in permutations('добрыня', r=6):
	w = ''.join(i)
	s = ''
	for q in w:
		if q in 'дбрн':
			s += 's'
		else:
			s += 'g'
	if s.count('s') > s.count('g') and 'gg' not in s:
		k += 1
print(k)

# 1440