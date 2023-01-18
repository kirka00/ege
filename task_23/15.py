def f(x, y, k, l):
	if x > y:
		return 0
	elif x == y and k > l:
		return 1
	elif x == y and k <= l:
		return 0
	return f(x + 1, y, k, l + 1) + f(x * 2, y, k + 1, l) + \
		f(x * 3, y, k + 1, l)


print(f(1, 157, 0, 0))
