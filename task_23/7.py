def f(x, k):
	if x == 34 and k == 8:
		return 1
	elif x > 34:
		return 0
	return f(x + 1, k + 1) + f(x * 2, k + 1) + f(x * 3, k + 1)


print(f(1, 0))
