def f(x, y, k1, k2):
	if x > y:
		return 0
	elif x == y:
		return 1
	if k1 == 2:
		return f(x * 2, y, 0, k2 + 1)
	if k2 == 2:
		return f(x + 1, y, k1 + 1, 0)
	return f(x + 1, y, k1 + 1, 0) + f(x * 2, y, 0, k2 + 1)
print(f(1, 14, 0, 0))
