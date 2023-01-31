from itertools import product
words = product('клрт', repeat=4)
k = []
for i in words:
	k.append(''.join(i))
print(k[66])
