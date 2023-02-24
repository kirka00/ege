from functools import lru_cache


@lru_cache
def f():
	for n in range(500_000, 1_000_001):
		d = 1
		k = 0
		dmax = 0
		while d * d <= n:
			if n % d == 0:
				if (n // d) - d <= 90:
					k += 1
					dmax = max(dmax, n // d)
				if k == 3:
					print(n, dmax)
					break
			d += 1


f()


'''
540540 780
619344 828
637560 840
752400 912
865800 975
889200 988
'''
