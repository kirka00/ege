def f(x, p):
	if x >= 43 or p > 2:
		return p == 2
	if p % 2:
		return (f(x + 1, p + 1) or f(x + 4, p + 1)) and f(x * 3, p + 1)
	else:
		return (f(x + 1, p + 1) or f(x + 4, p + 1)) or f(x * 3, p + 1)


print(min([i for i in range(43) if f(i, 0)]))


def f(x, p):
	if x >= 43 or p > 3:
		return p == 3
	if p % 2 == 0:
		return (f(x + 1, p + 1) or f(x + 4, p + 1)) and f(x * 3, p + 1)
	else:
		return (f(x + 1, p + 1) or f(x + 4, p + 1)) or f(x * 3, p + 1)


print(([i for i in range(43) if f(i, 0)]))


def f(x, p):
	if x >= 43 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return (f(x + 1, p + 1) or f(x + 4, p + 1)) and f(x * 3, p + 1)
	else:
		return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)


print(([i for i in range(43) if f(i, 0)]))
