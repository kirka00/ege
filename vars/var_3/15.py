def f(n, m, k):
	return max(n, m, k) < (n + m + k - max(m, n, k))


for a in range(1, 1000):
	for x in range(1, 1000):
		if not (not((f(x, 11, 18) == (not (max(x, 5) > 15))) and (f(x, a, 5)))):
			break
	else:
		print(a)


# 24 - true
