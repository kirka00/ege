from itertools import product
words = product('еклост', repeat=5)
k = 0
for i in words:
	k += 1
	word = ''.join(i)
	if word[0] == 'с' and 'оо' in word:
		print(k)
		break
