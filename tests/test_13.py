def f(s, c, m):
	if c == m: return 0
	if s >= 50: return c % 2 == m % 2
	h = [f(s + 2, c + 1, m)]

	return any(h) if (c + 1) % 2 == m % 2 else all(h)



for s in range(1, 50):
	for m in range(1, 5):
		if f(s, 0, m) == 1:
			if m == 2:
				print(s, m)
				break