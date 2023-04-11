for n in range(1, 1000):
	r = bin(n)[2:]
	if n % 3 == 0:
		r += r[-3:]
	else:
		r += bin(3 * (n % 3))[2:]
	q = int(r, 2)
	if q < 100:
		print(n)


# 22
