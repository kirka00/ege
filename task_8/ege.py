from itertools import product
from itertools import permutations

k = set()
words = permutations('авторота')
for i in words:
	word = ''.join(i)
	s = ''
	for c in word:
		if c in 'ао':
			s += 'g'
		else:
			s += 's'
	if 'gg' not in s and 'ss' not in s:
		k.add(word)

print(len(k))


k = set()
words = product('егеинф', repeat=6)
for i in words:
	word = ''.join(i)
	if word[0] == 'е' and word[-1] in 'эи' and word.count('фи') >= 2 \
		and word.count('егэ') == 0:
		k.add(word)

print(len(k))


k = []
words = product('аежймуa', repeat=4)
for i in words:
	k.append(''.join(i))
print(k.index('рамт') - k.index('март') + 1)
