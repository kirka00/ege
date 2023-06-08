for x in range(1, 50000):
	s = 4 ** 1014 - 2 ** x + 12
	if bin(s)[2:].count('0') == 2000:
		print(x)
		break