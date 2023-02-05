s = 4 ** 2022 - 6 * 4 * 522 + 5 * 64 ** 510 - 3 * 2 ** 330 - 100
n = ''
while s > 0:
	n += str(s % 8)
	s //= 8
print(str(n).count('7'))
# 1015 - true
