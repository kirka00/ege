for p in range(7, 100):
	for x in range(p):
		for y in range(p):
			for z in range(p):
				if (y * p ** 2 + 3 * p + y) + (y * p ** 2 + 6 * p + 5) == \
				x * p ** 3 + 2 * p ** 2 + z * p:
					print(x, y, z, p)
					exit()

print(int('17a', 12))  # 238