def f(x, y, p):
    if x + y >= 68 or p > 2:
        return p == 2
    return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x + y, y, p + 1) or \
    f(x, y + x, p + 1)
        

print(min([i for i in range(60) if f(8, i, 0)]))


def f(x, y, p):
	if x + y >= 68 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x + y, y, p + 1) and \
    f(x, y + x, p + 1)
	else:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x + y, y, p + 1) or \
    f(x, y + x, p + 1)
        

print(([i for i in range(54) if f(8, i, 0)]))


def f(x, y, p):
	if x + y >= 68 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x + y, y, p + 1) and \
    f(x, y + x, p + 1)
	else:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x + y, y, p + 1) or \
    f(x, y + x, p + 1)
        

print(min([i for i in range(60) if f(8, i, 0)]))
