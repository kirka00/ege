def f(x, y):
    return (x + y <= 22) or (y <= x - 6) or (y >= a)


for a in range(1000):
	if all(f(x, y) for x in range(1000) for y in range(1000)):
		print(a)


# 9