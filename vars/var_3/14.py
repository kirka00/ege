n = 243 ** 540 - 6 * 9 ** 530 + 21 * 3 ** 511 - 3 ** 70 - 200
s = ''
while n > 0:
	s += str(n % 9)
	n //= 9
print(s.count('8'))


# 1071 - true
