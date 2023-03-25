def f(x, y, p1, p2):
	if x > y:
		return 0
	if x == y:
		return 1
	if p1 == p2 == 0 or p1 != p2:
		return f(x + 1, y, p2, 1) + f(x * 2, y, p2, 2)
	if p1 == p2 == 1:
		return f( x * 2, y, p2, 2)
	if p1 == p2 == 2:
		return f(x + 1, y, p2, 1)


print(f(1, 14, 0, 0))


# 6
