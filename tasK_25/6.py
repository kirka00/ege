for n in range(50034679, 92136896):
	k = 0
	if round(n ** 0.5) == n ** 0.5:
		for d in range(2, round(n ** 0.5)):
			if n % d == 0:
				k += 2
				dmax = n // d
		if k == 2:
			print(n, dmax)

print('----------------')
def f(n):
	for d in range(2, round(n ** 0.5) + 1):
		if n % d == 0:
			return False
	return True


for q4 in range(round(50034679 ** 0.25), round(92136896 ** 0.25) + 1):
	x = q4 ** 4
	if 50034679 <= x <= 92136896 and f(q4):
		print(x, max([q4, q4 ** 2, q4 ** 3]))


'''
62742241 704969
88529281 912673
'''
