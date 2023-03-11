for x in range(103_000_000, 104_000_001):
	ans = set()
	for d in range(1, round(x ** 0.5) + 1):
		if x % d == 0 and d % 2:
			ans.add(d)
			ans.add(x // d)
			if len(ans) > 3:
				break
	print(ans)


def prost(n):
	for d in range(2, round(n ** 0.5) + 1):
		if n % d == 0:
			return False
	return True


primes = set()
for i in range(3, int(63_000_000**0.25) + 1):
    if prost(i):
        primes.add(i)

for i in range(103_000_000, 104_000_001):
	x = i
	while x % 2 == 0:
		x //= 2
	q4 = int(x ** 0.25)
	if q4 in primes and q4 ** 4 == x:
		print(i, x)


'''
63123848 7890481
66724352 130321
71639296 279841
'''
