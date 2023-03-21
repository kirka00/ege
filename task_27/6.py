with open('files/dz_6/b.txt') as f:
	n = int(f.readline())
	tailsum = [0] + 2 * [None]
	maxsumma = summa = count = 0
	for i in range(n):
		x = int(f.readline())
		summa += x
		if x % 5 == 0:
			count += 1
		d = count % 3
		if tailsum[d] is None:
			tailsum[d] = summa
		if count >= 3:
			maxsumma = max(maxsumma, summa - tailsum[d])
print(maxsumma)


# 66453 69995639
