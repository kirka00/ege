def f(x, y):
	if x > y:
		return 0
	if x == y:
		return 1
	return f(x + 2, y) + f(x * 2, y) + f(x * 3, y)

print(f(1, 6) * f(6, 24))


# 40 - true
