s = 7 ** 80 + 49 ** 15 - 49
n = ''
while s > 0:
	n += str(s % 7)
	s //= 7
print(n.count('6'))


# 28 - true
