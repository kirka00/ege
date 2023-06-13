def f(x):
	ans = set()
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			ans |= {d, x // d}
	return sorted(ans)


for i in range(150_001, 151_100):
	s = sum(f(i))
	if s % 13 == 10:
		print(i, s)

