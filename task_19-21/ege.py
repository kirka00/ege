'''print('w x y z')
for w in range(2):
	for x in range(2):
		for y in range(2):
			for z in range(2):
				if not((not(z <= w)) or x or (not y)):
					print(w, x, y, z)'''


'''def f(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return n + 3 * f(n - 1)
	if n > 1:
		return 2 + 2 * f(n - 2)


print(f(23))'''

# 19
def f(x, y, p):
	if x + y >= 118 or p > 2:
		return p == 2
	return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) \
		or f(x, y * 2, p + 1)

print(min([i for i in range(1, 114) if f(3, i, 0)]))

# 20
def f(x, y, p):
	if x + y >= 118 or p > 3:
		return p == 3
	if p % 2:
		return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) \
			and f(x, y * 2, p + 1)
	else:
		return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) \
			or f(x, y * 2, p + 1)


print([i for i in range(1, 114) if f(3, i, 0)])

# 21


def f(x, y, p):
	if x + y >= 118 or p > 4:
		return p == 2 or p == 4
	if p % 2 == 0:
		return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) \
			and f(x, y * 2, p + 1)
	else:
		return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) \
			or f(x, y * 2, p + 1)


print(min([i for i in range(1, 114) if f(3, i, 0)]))


def f(x, y):
	if x < y:
		return 0
	if x == y:
		return 1
	return f(x - 1, y) + f(x % 2, y)
print(f(31, 12) + f(12, 2))
