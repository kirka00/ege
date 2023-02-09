s = 5 ** 2022 - 2 * 5 ** 1010 + 25 ** 850 + 2500
new = ''
while s > 0:
	new += str(s % 5)
	s //= 5
print(new.count('4'))


# 690 - true
