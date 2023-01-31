from itertools import product

k = set()
words = product('слон', repeat=5)
for i in words:
	word = ''.join(i)
	if word.count('с') == 1:
		k.add(word)

print(len(k))
