# 19
def f(x, y, p):
    if x + y >= 69 and p > 2:
        return p == 2
    return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) \
        or f(x, y * 2, p + 1)


print(min([i for i in range(1, 63) if f(6, i, 0)]))


# 20
def f(x, y, p):
    if x + y >= 69 or p > 3:
        return p == 3
    if p % 2:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and \
            f(x * 2, y, p + 1) and f(x, y * 2, p + 1)
    else:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) \
            or f(x, y * 2, p + 1)


print(([i for i in range(1, 63) if f(6, i, 0)]))


# 21
def f(x, y, p):
	if x + y >= 69 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and \
			f(x * 2, y, p + 1) and f(x, y * 2, p + 1)
	else:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) \
			or f(x, y * 2, p + 1)


print(([i for i in range(1, 63) if f(6, i, 0)]))
