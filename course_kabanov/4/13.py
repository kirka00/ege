for n in range(1, 20):
	try:
		if int('132', n) + int('13', 8) == int('124', n + 1):
			print(n)
	except:
		pass
        