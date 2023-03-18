with open('files/dz_1/b.txt') as f:
	max6, maxNo6, = 0, 0
	n = int(f.readline())
	for i in range(n):
		a = int(f.readline())
		if a % 6 != 0 and a > maxNo6:
			maxNo6 = a
		if a % 6 == 0 and a > max6:
			max6 = a
	if max6 * maxNo6 == 0:
		print('1')
	else:
		print(max6 * maxNo6)


# 782040 995004
