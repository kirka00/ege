k = 0
for n in range(1, 10000):
	if 16 <= n < 625 and n % 16 == 12:
		k += 1


print(k)


# 38