x = 81 ** 2017 + 9 ** 5223 - 81
k = 0
while x > 0:
	if x % 9 == 8:
		k += 1
	x //= 9
print(k)
