for n in range(1000):
	n = n - (n % 8) + (n % 2)
	i = bin(n)[2:]
	for _ in range(2):
		i += str(sum(map(int, i)) % 2)
	if int(i, 2) > 97:
		print(int(i, 2))
		break


# 102 - true
