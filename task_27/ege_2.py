with open('files/7/27-71b.txt') as f:
	n = int(f.readline())
	min_sum = 69 * [10 ** 10]
	min_len = 69 * [0]
	summa, maxsum, minlenght, ms, ln = 0, 0, 0, 0, 0
	for i in range(n):
		summa += int(f.readline())
		d = summa % 69
		if d == 0:
			maxsum = summa
			minlenght = i
		else:
			ms = summa - min_sum[d]
			ln = i - min_len[d]
			if ms > maxsum or (ms == maxsum and ln < minlenght):
				maxsum = ms
				minlenght = ln
		if summa < min_sum[d]:
			min_sum[d] = summa
			min_len[d] = i
print(minlenght)


# 14 99989
