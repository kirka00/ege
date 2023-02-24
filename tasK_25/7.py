def f(n):
	for d in range(2, round(n ** 0.5) + 1):
		if n % d == 0:
			return False
	return True


for i in range(63_000_000, 75_000_001):
	x = i
	while x % 2 == 0:
		x //= 2
	q4 = round(x ** 0.25)
	if f(q4) and q4 ** 4 == x:
		print(i, x)


'''
63123848 7890481
66724352 130321
67108864 1
71639296 279841
'''
