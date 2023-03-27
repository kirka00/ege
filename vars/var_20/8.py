from itertools import product


words = product('abcd', repeat=4)
k = 0
for i in words:
	word = ''.join(i)
	if word.count('a') == 2:
		k += 1
print(k)


# 54 - true
