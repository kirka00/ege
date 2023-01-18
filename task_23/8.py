def f(x, y):
	if x < y:
		return 0
	elif x == y:
		return 1
	else:
		if x != 2 ** (len(bin(x)[2:]) - 1):
			return f(x - 1, y) + f(2 ** (len(bin(x)[2:]) - 1), y)
		else:
			return f(x - 1, y)


print(f(int('1000000', 2), int('1000', 2)))
