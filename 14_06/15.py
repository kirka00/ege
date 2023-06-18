def f(x):
	return (x % 10 == 0) and (x % 26 == 0) and (x >= 300) and (a <= x)

for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
