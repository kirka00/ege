s = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1
new = ''
while s > 0:
	new += str(s % 9)
	s //= 9
print(new.count('0'))


# 1007 - true
