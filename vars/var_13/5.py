for i in range(1000):
	n = i - (i % 8) + i % 2
	n = bin(n)[2:]
	for i in range(2):
		summa = sum(map(int, n))
		n = n + str(summa % 2)
	if int(n, 2) > 90:
		print(int(n, 2))
		break


# 96 - true
