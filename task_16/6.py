def f(n):
	if n <= 13:
		return n ** 3 + n * n + 1
	else:
		if n % 3 == 0:
			return f(n - 1) + 2 * n * n - 3
		else:
			return f(n - 2) + 3 * n + 6


k = 0
for n in range(1, 1001):
	values = str(f(n))
	if len(values) == len([i for i in values if int(i) % 2]):
		k += 1

print(k)
