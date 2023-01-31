from itertools import product

k = set()
words = product('каракас', repeat=6)
for i in words:
	word = ''.join(i)
	if word.count('к') + word.count('р') + word.count('с') >= 3:
		k.add(word)

print(len(k))
