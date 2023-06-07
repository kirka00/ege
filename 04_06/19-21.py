def f(x, y, p):
	if x + y >= 159 or p > 2:
		return p == 2
	return f(x + 1, y, p + 1) or f(x + 3, y, p + 1) or \
			f(x, y + 1, p + 1) or f(x, y + 3, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)


print(min([i for i in range(1, 131) if f(7, i, 0)]))


def f(x, y, p):
	if x + y >= 159 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 1, y, p + 1) and f(x + 3, y, p + 1) and \
				f(x, y + 1, p + 1) and f(x, y + 3, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)
	else:
		return f(x + 1, y, p + 1) or f(x + 3, y, p + 1) or \
				f(x, y + 1, p + 1) or f(x, y + 3, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)


print(([i for i in range(1, 131) if f(7, i, 0)]))


def f(x, y, p):
	if x + y >= 159 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return f(x + 1, y, p + 1) and f(x + 3, y, p + 1) and \
				f(x, y + 1, p + 1) and f(x, y + 3, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)
	else:
		return f(x + 1, y, p + 1) or f(x + 3, y, p + 1) or \
				f(x, y + 1, p + 1) or f(x, y + 3, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
	

print(min([i for i in range(1, 131) if f(7, i, 0)]))


'''
38
[	, 74, 75]
71
'''