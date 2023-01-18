def f(x, y):  # спросить про эту задачу (сложно)
	if x < y:
		return 0
	elif x == y:
		return 1
	else:
		if x % 3 == 0:
			return f(x - 2, y)
		else:
			return f(x - 2, y) + f(x - x % 3, y)


print(f(int('212', 3), int('10', 3)))
