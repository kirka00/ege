from itertools import product


words = product('аблор', repeat=4)
k = 0
for word in words:
	i = ''.join(word)
	k += 1
	if i[0] == 'л':
		print(k)
		break


# 251
