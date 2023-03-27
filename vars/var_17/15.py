def f(x, y):
    return (3 * x + y < a) or (x < y) or (16 <= x)


for a in range(1, 1000):
	if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
		print(a)
		break


# 61 - true
