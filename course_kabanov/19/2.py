def f(x, p):
	if x >= 36 or p > 2:
		return p == 2
	if p % 2:
		return f(x + 1, p + 1) and (x * 2, p + 1) and (x * 3, p + 1)
	else:
		return f(x + 1, p + 1) or (x * 2, p + 1) or (x * 3, p + 1)


print(([i for i in range(36) if f(i, 0)]))