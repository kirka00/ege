with open('files/24-s1.txt') as f:
	k = 0
	for x in f:
		if x.count('K') > x.count('U'):
			k += 1
print(k)


# 470
