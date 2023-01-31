from itertools import permutations

k = set()
words = permutations('есаул')
for i in words:
	word = ''.join(i)
	if 'еа' not in word and 'ае' not in word and 'ау' not in word \
		and 'уа' not in word and 'еу' not in word and 'уе' not in word:
		k.add(word)

print(len(k))
