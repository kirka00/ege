def f(x):
	return (((x % 20 == 0) <= (x % 11 != 0)) or (x + a >= 300))

for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		print(a)
		break
# 80 - true
