def f(x, y):
	if x > y:
		return 0
	elif x == y:
		return 1
	else:
		if str(x)[-2] == '9':
			return f(x + 1, y)
		else:
			return f(x + 1, y) + f(x + 10, y)


print(f(12, 36))
