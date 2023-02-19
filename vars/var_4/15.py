def f(n,m, k):
	return n + m > k and n + k > m and m + k > n

for a in range(1, 1000):
	for x in range(1, 1000):
		if (not ((f(x, 12, 20) == (not (max(x, 5) > 28))) and (f(x, a, 3)))) == False:
			break
	else:
		print(a)


# 6 - true
