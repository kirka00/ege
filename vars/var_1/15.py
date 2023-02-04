def f(x):
	return ((x % 13 == 0) <= (x % 21 != 0)) or (x + a >= 500)


for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break
# true
