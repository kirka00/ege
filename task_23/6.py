def f(x, y):
	if x > y:
		return 0
	elif x == y:
		return 1
	else:
		return f(x + 1, y) + f(x * 2, y)


print(f(5, 15) + f(5, 30))
