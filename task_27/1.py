with open('files/dz_1/b.txt') as f:
	max7, maxNo7, = 0, 0
	n = int(f.readline())
	for i in range(n):
		a = int(f.readline())
		if a % 6 != 0 and a > maxNo7:
			maxNo7 = a
		if a % 6 == 0 and a > max7:
			max7 = a
	if max7 * maxNo7 == 0:
		print('1')
	else:
		print(max7 * maxNo7)


# 782040 995004
