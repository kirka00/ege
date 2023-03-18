with open('files/dz_4/b.txt') as f:
	n = int(f.readline())
	summa = [0 for i in range(10)]
	for i in range(n):
		a, b = map(int, f.readline().split())
		sums = [10 ** 10] * 10
		for s in summa:
			for x in a, b:
				summatek = s + x
				if summatek < sums[summatek % 10]:
					sums[summatek % 10] = summatek
		summa = sums[:]
print(summa[0])


# 8030 19596700
