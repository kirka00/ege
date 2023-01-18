def f(n):
	if n <= 5:
		return n
	else:
		if n % 4 == 0:
			return n + f(n / 2 - 1)
		else:
			return n + f(n + 2)


for n in range(1, 10000):
	try:
		f(n)
		print(n)
	except:
		pass
