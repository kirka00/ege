for i in range(1, 1000):
	n = bin(i)[2:]
	r = n
	for _ in range(3):
		if sum([int(j) for j in str(r)]) % 2 != 0:
			n += '1'
		else:
			n += '0'
		r = int(n, 2)
	if r > 1028:
		print(r)
		break


# 1035
