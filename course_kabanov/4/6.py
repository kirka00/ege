for x in range(1, 50000):
	s = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
	if bin(s)[2:].count('1') == 500:
		print(x)
		break