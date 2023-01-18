def f(x, y, command):
	if x > y:
		return 0
	elif x == y:
		return 1
	else:
		if command == 0:
			return f(x + 1, y, 1) + f(x + 2, y, 0) + f(x * 2, y, 0)
		else:
			return f(x + 2, y, 0) + f(x * 2, y, 0)

print(f(1, 18, 0))
