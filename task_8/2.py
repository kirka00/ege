from itertools import product

k = set()
words = product('берклий', repeat=4)
for i in words:
	word = ''.join(i)
	if word[0] != 'й' and (word.count('и') + word.count('е') >= 1):
		k.add(word)

print(len(k))
