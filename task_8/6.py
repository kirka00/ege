from itertools import product

k = set()
words = product('0123456789', repeat=7)
for i in words:
	word = ''.join(i)
	s = ''
	for c in word:
		if c in '02468':
			s += 'ч'
		else:
			s += 'н'
	if 'чч' not in s and 'нн' not in s and word[0] != '0' and word[-1] in '50' and len(set(word)) == 7:
		k.add(word)
print(len(k))
