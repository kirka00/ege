def f(x, p):
	if x > 33 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x + 3, p + 1) \
				and f(x * 2, p + 1)
	else:
		return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x + 3, p + 1) \
				or f(x * 2, p + 1)


print(([i for i in range(1, 34) if f(i, 0)]))




