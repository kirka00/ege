def f(x, y):
    return (3 * x + 4 * y != 60) or ((a >= x) and (a >= y))


for a in range(1, 1000):
	if all(f(x, y) == True for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
		break
