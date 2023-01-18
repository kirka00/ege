def f(x, y):
	return (5 * y + 3 * x != 110) or (x > a) or (2 * y > a)

for a in range(1, 1000):
	if all(f(x, y) == True for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
