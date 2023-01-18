def f(x, y):
	if x > y:
		return 0
	elif x == y:
		return 1
	else:
		if x % 2 != 0:
			return f(x + 1, y)
		else:
			return f(x + 1, y) + f(x * 1.5, y)



print(f(1, 20))
