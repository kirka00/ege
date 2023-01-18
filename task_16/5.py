def f(n):
	if n > 25:
		return n * n + 4 * n + 3
	else:
		if n % 3 == 0:
			return f(n + 1) + 2 * f(n + 4)
		else:
			return f(n + 2) + 3 * f(n + 5)

k = 0
for n in range(1, 1001):
	if sum(map(int, str(f(n)))) == 24:
		k += 1

print(k)
