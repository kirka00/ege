from itertools import product
words = product('дкмо', repeat=5)
k = []
for i in words:
	k.append(''.join(i))
print(k.index('комод') - k.index('домок') + 1)
