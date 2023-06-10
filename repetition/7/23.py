def f(x, y, k=0, h18=0):
	if x == 18: h18 = True
	if x > y or x == 11 or x == 35:
		return 0
	if x == y:
		return 1 if k <= 5 and h18 else 0
	return f(x + 1, y, k + 1, h18) + f(x + 3, y, k, h18) + f(x * 2, y, k, h18)


print(f(2, 40))


# 3505