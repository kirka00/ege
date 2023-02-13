def f(n):
	if n < 3:
		return 1
	if n > 2 and n % 2:
		return f(n - 1) + f(n -2)
	if n > 2 and n % 2 == 0:
		s = 0
		for i in range(1, n):
			s += f(i)
		return s
print(f(24))


# 887040 - true
