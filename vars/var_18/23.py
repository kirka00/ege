def f(x, y):
	if x > y:
		return 0
	if x == y:
		return 1
	return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)


print(f(3, 8) * f(8, 11) * f(11, 14))


# 24 - true
