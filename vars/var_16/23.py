def f(x, y):
	if x > y:
		return 0
	if x == y:
		return 1
	return f(x + 5, y) + f(x + 4, y) + f(x * 3, y)


print(f(2, 6) * f(6, 30))



# 16 - true
