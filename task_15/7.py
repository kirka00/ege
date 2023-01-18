def f(x):
	return (a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0)))


k = 0
for a in range(1, 1000):
	if all(f(x) for x in range(1, 1000)):
		k += 1
print(k)
