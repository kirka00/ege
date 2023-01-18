def f(x):
	return (x % a == 0) <= ((x % 14 == 0) and (x % 21 == 0))

for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break
