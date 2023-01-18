def f(x, y):
	return (3 * y + x < a) or (x > 12) or (y > 15)


for a in range(1, 1000):
	if all(f(x, y) == True for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
		break
