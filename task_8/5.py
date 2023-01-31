from itertools import permutations

k = set()
words = permutations('акарида')
for i in words:
	word = ''.join(i)
	s = ''
	for c in word:
		if c in 'аи':
			s += 'g'
		else:
			s += 's'
	if 'gg' not in s and 'ss' not in s:
		k.add(word)

print(len(k))
