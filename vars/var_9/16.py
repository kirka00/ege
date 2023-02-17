def f(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return n + 2 * f(n - 1)
	if n > 1 and n % 2:
		return 1 + 3 * f(n - 1)
print(f(17))


# 4434175 - почему-то неверно
