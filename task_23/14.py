def f(x, y, k):
	if x > y:
		return 0
	elif x == y:
		return 1
	if k < 2:
		return f(x + 1, y, k) + f(x * 2, y, k + 1) + f(x * 3, y, k + 1)
	else:
		return f(x + 1, y, k)


print(f(1, 100, 0))
