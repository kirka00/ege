def f(x, y):
	if x > y:
		return 0
	if x == y:
		return 1
	return f(x + 2, y) + f(x + 7, y)

print(f(5, 	49))

# 639 - true
