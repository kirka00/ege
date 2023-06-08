for i in range(1, 1000):
	s = 125 ** 200 - 5 ** i + 74
	q = ''
	while s > 0:
		q += str(s % 5)
		s //= 5
	if q.count('4') == 100:
		print(i)
		break