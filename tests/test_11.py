def f(s, c, m):
	if s >= 30: return c % 2 == m % 2
	if c == m: return 0

	h = [f(s + 2, c + 1, m), f(s + 3, c + 1, m), f(s * 2, c + 1, m)]


	return any(h) if (c + 1) % 2 == m % 2 else all(h)



for s in range(1, 30):
	for m in range(1, 5):
		if f(s, 0, m) == 1:
			print(s, m)
			break

print('------')
def f(x, p):
	if x >= 30 or p > 2:
		return p == 2
	if p % 2 == 0:
		return f(x + 2, p + 1) and f(x + 3, p + 1)  and f(x * 2, p + 1)
	else:
		return f(x + 2, p + 1) or f(x + 3, p + 1)  or f(x * 2, p + 1)


print(min([i for i in range(30) if f(i, 0)]))


def f(x, p):
	if x >= 30 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 2, p + 1) and f(x + 3, p + 1)  and f(x * 2, p + 1)
	else:
		return f(x + 2, p + 1) or f(x + 3, p + 1)  or f(x * 2, p + 1)


print(([i for i in range(30) if f(i, 0)]))


def f(x, p):
	if x >= 30 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return f(x + 2, p + 1) and f(x + 3, p + 1)  and f(x * 2, p + 1)
	else:
		return f(x + 2, p + 1) or f(x + 3, p + 1)  or f(x * 2, p + 1)


print(([i for i in range(30) if f(i, 0)]))