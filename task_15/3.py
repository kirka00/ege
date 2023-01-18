def f(x):
	return (x & 87 == 0) <= ((x & 31 != 0) <= (x & a != 0))


for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break
