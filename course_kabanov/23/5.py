def f(x):
	ans = set()
	for d in range(2, round(x ** 0.5) + 1):
		if x % d == 0:
			ans |= {d, x // d}
	return sorted(ans)


for i in range(250_201, 255_500):
    w = f(i)
    if w:
        s = max(w) + min(w)
    if s % 123 == 17:
        print(i, s)

