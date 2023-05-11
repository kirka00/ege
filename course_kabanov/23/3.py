def f(x):
	ans = set()
	for d in range(1, round(x ** 0.5) + 1):
		if x % d == 0:
			ans |= {d, x // d}
	return sorted(ans)


for i in range(154026, 154044):
	w = f(i)
	if len(w) == 4:
		print(w[2], w[3])
