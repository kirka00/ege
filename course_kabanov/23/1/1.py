def f(x):
	ans = set()
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			ans |= {d, x // d}
	return sorted(ans)


for i in range(174457, 174505):
	w = f(i)
	if len(w) == 2:
		print(w[0], w[1])
