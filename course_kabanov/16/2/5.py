def f(n):
	if n >= 1000:
		return n
	else:
		if n % 3 == 0:
			return n + f(n // 3)
		else:
			return 2 * n + f(n + 3)
print(f(999) - f(46))