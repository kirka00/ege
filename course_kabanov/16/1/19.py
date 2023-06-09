def f(n):
	if n <= 1:
		return n
	else:
		if n % 3 == 0:
			return n + f(n // 3)
		else:
			return n + f(n + 3)
		
for i in range(1, 1000):
	try:
		if f(i) > 100:
			print(i)
			break
	except:
		pass
