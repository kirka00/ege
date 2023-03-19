with open('files/dz_1/b.txt') as f:
	maxX, max2, max3, max6 = 0, 0, 0, 0
	n = int(f.readline())
	for i in range(n):
		a = int(f.readline())
		if a % 6 == 0 and a > max6:
			if max6 > maxX:
				maxX = max6
			max6 = a
		else:
			if a > maxX:
				maxX = a
			if a % 2 == 0 and a > max2:
				max2 = a
			elif a % 3 == 0 and a > max3:
				max3 = a
	r = max(max6 * maxX, max2 * max3)
	print(max6, maxX, max6 * maxX)
	print(max2, max3, max2 * max3)
	print(r)


# 782040 997002
