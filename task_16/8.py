def f(n):
	if n <= 5:
		return n
	else:
		if n % 5 == 0:
			return n + f(n / 5 + 1)
		else:
			return n + f(n + 6)


for n in range(1, 10000):
	try:
		if f(n) > 1000:
			print(n)
			break
	except:
		pass
