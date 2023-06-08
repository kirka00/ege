for x in range(1, 50000):
	s = 36 ** 17 - 6 ** x + 71
	q = ''
	while s > 0:
		q += str(s % 6)
		s //= 6
	if sum([int(i) for i in q]) == 61:
		print(x)
		break