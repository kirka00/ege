def f(s, c, m):
	if 72 >= s >= 43: return c % 2 == m % 2
	if s > 72: return c % 2 != m % 2
	if c == m: return 0

	h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m)]

	return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 43):
	for m in range(1, 5):
		if f(s, 0, m) == 1:
			if m == 2:
				print(s, m)
			if m == 3:
				print(s, m)
			if m == 4:
				print(s, m)
			break