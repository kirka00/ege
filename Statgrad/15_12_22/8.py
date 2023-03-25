from itertools import product

words = product('вероника', repeat=6)

k = 0
for i in words:
	word = ''.join(i)
	if (word.count('е') + word.count('о') + word.count('и') + \
		word.count('а')) > (word.count('в') + word.count('р') + \
		word.count('н') + word.count('к')):
			k += 1
print(k)


# 90112
